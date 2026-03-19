from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

import json
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from .models import Course, Account
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, SignUpForm
from django.shortcuts import render, redirect
from . import account
from .models import Account, Product, Course
from .cart import (
    get_or_create_cart,
    add_product_to_cart,
    decrease_product_from_cart,
    remove_product_from_cart,
    update_status
)

from . import product as product_service


from rest_framework.response import Response
from rest_framework.decorators import api_view  

#data oject will be data from the database. 
data = {"U1" : "asd@example.com", "U2": "asd2@example.com"}

def index(request):
    return HttpResponse("courses index page")

def render_html(request) : 
    courses = Course.objects.all() # <----- Getting all rows of the course table
    context = {'courses': courses} # <----- {name of the list: the list of rows}
    
    return render(request, 'index.html', context) # <----- pass the "context" to the index.html file


@api_view(['GET'])
def get_user_data(request):
    
    return Response(data)

@api_view(['DELETE'])
def delete_user_data(request):
    data.popitem()
        
    return HttpResponse("an account has been removed")

@api_view(['POST'])
def post_user_data(request):
    
    return Response(data)
    return render(request, 'index.html', context) # <----- pass the "context" to the index.html file

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account.create_account(name=name, email=email, password=make_password(raw_password))
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            user = account.get_account_by_email(email)

            if user is not None and check_password(password, user.password):
                messages.success(request, 'Login successful.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# --- Cart API ---

def get_cart(request, account_id):
    account = Account.objects.get(id=account_id)
    cart = get_or_create_cart(account)

    items = []
    for item in cart.items.all():
        items.append({
            "product_id": item.product.id,
            "name": item.product.name,
            "price": float(item.product.price),
            "quantity": item.item_quantity
        })

    return JsonResponse({
        "status": cart.status,
        "items": items
    })

@csrf_exempt
def add_to_cart(request):
    data = json.loads(request.body)
    account = Account.objects.get(id=data["account_id"])
    product = Product.objects.get(id=data["product_id"])
    quantity = data.get("quantity", 1)

    add_product_to_cart(account, product, quantity)
    return JsonResponse({"message": "Product added"})

@csrf_exempt
def decrease_from_cart(request):
    data = json.loads(request.body)
    account = Account.objects.get(id=data["account_id"])
    product = Product.objects.get(id=data["product_id"])
    quantity = data.get("quantity", 1)

    decrease_product_from_cart(account, product, quantity)
    return JsonResponse({"message": "Product decreased"})

@csrf_exempt
def remove_from_cart(request):
    data = json.loads(request.body)
    account = Account.objects.get(id=data["account_id"])
    product = Product.objects.get(id=data["product_id"])

    remove_product_from_cart(account, product)
    return JsonResponse({"message": "Product removed"})

@csrf_exempt
def checkout(request):
    data = json.loads(request.body)
    account = Account.objects.get(id=data["account_id"])

    update_status(account, "checked_out")
    return JsonResponse({"message": "Checked out"})



# --- Product API (@api_view) ---

def product_to_dict(p):
    #Convert a Product model instance to a JSON dict
    return {
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": str(p.price),
        "stock": p.stock_quantity,
        "origin": p.origin_country,
        "image": p.image if p.image else ""
    }


@api_view(['GET', 'POST'])
def product_list(request):
    
    #GET  /api/products/  → list all products
    #POST /api/products/  → create a new product
    
    if request.method == 'GET':
        products = product_service.get_all_products()
        return Response([product_to_dict(p) for p in products])

    # POST — request.data is already parsed by DRF
    p = product_service.create_product(
        name=request.data["name"],
        description=request.data.get("description", ""),
        price=request.data["price"],
        stock=request.data.get("stock", 0),
        origin=request.data.get("origin", ""),
    )
    return Response(product_to_dict(p), status=status.HTTP_201_CREATED)


@api_view(['GET', 'PATCH', 'DELETE'])
def product_detail(request, pk):
    
    # GET    /api/products/<pk>/  → retrieve one product
    # PATCH  /api/products/<pk>/  → update
    # DELETE /api/products/<pk>/  → delete
    
    p = product_service.get_product_by_id(pk)
    if p is None:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(product_to_dict(p))

    if request.method == 'PATCH':
        data = request.data
        if "name" in data:
            p = product_service.update_product_name(pk, data["name"])
        if "description" in data:
            p = product_service.update_product_description(pk, data["description"])
        if "price" in data:
            p = product_service.update_product_price(pk, data["price"])
        if "stock" in data:
            p = product_service.update_product_stock(pk, data["stock"])
        if "origin" in data:
            p = product_service.update_product_country(pk, data["origin"])
        return Response(product_to_dict(p))

    if request.method == 'DELETE':
        # DELETE
        product_service.delete_product(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

