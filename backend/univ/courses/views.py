import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Account, Product, Course
from .cart import (
    get_or_create_cart,
    add_product_to_cart,
    decrease_product_from_cart,
    remove_product_from_cart,
    update_status
)

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