from django.shortcuts import render, HttpResponse , redirect
from .models import Product
from django.contrib.auth import login , authenticate
from django import forms 
from django.contrib import messages
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout


def index(request):
    context = {
        "products" : Product.objects.all()
    }	
    return render(request, "first_app/index.html" , context)


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if (form.is_valid() and form.cleaned_data.get('password') == form.cleaned_data.get('confirm_password')  ) :
            user = form.save(commit=False)
            user.active=True
            user.staff=False
            user.admin=False
            user.set_password(user.password)
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            print(form.cleaned_data)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        elif (form.cleaned_data.get('password') != form.cleaned_data.get('confirm_password') ):
              form.add_error('confirm_password', 'The passwords do not match')
    else:
        form = UserForm()
    return render(request, "first_app/signup.html" , {'form' : form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None: 
                form = login(request, user) 
                # messages.success(request, f' wecome {username} !!') 
                return redirect('/')
            else: 
                messages.info(request, f'account does not exist')   
    form = LoginForm()
    return render(request, "first_app/login.html" , {'form' : form})


def detail(request , id):
    product = Product.objects.get(id= id)
    context = {
        "product" : product
    }	
    return render(request, "first_app/product_details.html" , context)

def add_product(request):
    if request.method == "POST":
        form = addform(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = addform()
    return render(request , "first_app/admin.html", {'form' : form} )


def user_logout(request):
    logout(request)
    return redirect(index)