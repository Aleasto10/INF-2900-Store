import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

def render_html(request): 
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'index.html', context)

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

