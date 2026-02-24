from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

def index(request):
    return HttpResponse("courses index page")


def render_html(request) : 
    courses = Course.objects.all() # <----- Getting all rows of the course table
    context = {'courses': courses} # <----- {name of the list: the list of rows}
    return render(request, 'index.html', context) # <----- pass the "context" to the index.html file