from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'shop/index.html')
def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("Contact")

def tracker(request):
    return HttpResponse("Tracker")

def search(request):
    return HttpResponse("Search")

def productview(request):
    return HttpResponse("Product View")

def checkout(request):
    return HttpResponse("Checkout")