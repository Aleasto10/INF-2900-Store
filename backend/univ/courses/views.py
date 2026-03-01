from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from .models import Course, Account
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
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


def index(request):
    return HttpResponse("courses index page")

def render_html(request) : 
    courses = Course.objects.all() # <----- Getting all rows of the course table
    context = {'courses': courses} # <----- {name of the list: the list of rows}
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



def product_list(request):
    #API endpoint: /api/products/
    products = product_service.get_all_products()
    data = [
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": str(p.price),        # Decimal → string for JSON
            "stock": p.stock_quantity,
            "origin": p.origin_country,
        }
        for p in products
    ]
    return JsonResponse(data, safe=False)
