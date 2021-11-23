from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request,'register.html', context)


def login(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'inicio de sesion con exito')
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request,'login.html', context)