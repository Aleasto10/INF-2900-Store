from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

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