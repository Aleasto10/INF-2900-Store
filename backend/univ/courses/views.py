from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Course
from . import product as product_service

def index(request):
    return HttpResponse("courses index page")


def render_html(request) : 
    courses = Course.objects.all() # <----- Getting all rows of the course table
    context = {'courses': courses} # <----- {name of the list: the list of rows}
    return render(request, 'index.html', context) # <----- pass the "context" to the index.html file


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