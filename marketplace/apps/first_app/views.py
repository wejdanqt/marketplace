from django.shortcuts import render, HttpResponse , redirect
from .models import Product

from .forms import addform

def index(request):
    context = {
        "products" : Product.objects.all()
    }	
    return render(request, "first_app/index.html" , context)

def viewp(request):
 
    return render(request, "first_app/product_details.html")


def detail(request , id):
    product = Product.objects.get(id= id)
    context = {
        "product" : product
    }	
    return render(request, "first_app/product_details.html" , context)

def admin(request):
    form = addform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, "first_app/admin.html" , context)


def add_product(request):
    if request.method == "POST":
        form = addform(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = addform()
    return render(request , "first_app/admin.html", {'form' : form} )



    return redirect(index)

