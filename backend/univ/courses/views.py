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