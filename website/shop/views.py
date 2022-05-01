from django.shortcuts import get_object_or_404, render
from . import models

from cart.cart import Cart

# Create your views here.

def index(request):
  Cart(request)
  product_list = models.Product.objects.all()[:5]
  return render(request,'index.html',{'product_list':product_list})

def checkout(request):
  return render(request,'checkout.html')

def product(request,pk):
  product_detail = get_object_or_404(models.Product,id=pk)
  return render(request,'product.html',{'product_detail':product_detail})

def store(request):
  return render(request,'store.html')