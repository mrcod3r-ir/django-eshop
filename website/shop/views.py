from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
  product_list = models.Product.objects.all()[:5]
  return render(request,'index.html',{'product_list':product_list})

def checkout(request):
  return render(request,'checkout.html')

def product(request):
  return render(request,'product.html')

def store(request):
  return render(request,'store.html')