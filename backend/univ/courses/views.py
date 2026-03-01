from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

from rest_framework.response import Response
from rest_framework.decorators import api_view  


def index(request):
    return HttpResponse("courses index page")


def render_html(request) : 
    courses = Course.objects.all() # <----- Getting all rows of the course table
    context = {'courses': courses} # <----- {name of the list: the list of rows}
    return render(request, 'index.html', context) # <----- pass the "context" to the index.html file


@api_view(['GET'])
def get_user_data(request):
    # This is your "method" logic
    data = {"name": "Alex", "status": "Active"}
    return Response(data)