from django.shortcuts import redirect, render,reverse,get_object_or_404
from .cart import Cart
from shop import models

# Create your views here.

def cart_add(request):
  cart = Cart(request)
  product = get_object_or_404(models.Product,id=2)
  cart.add(product)
  return redirect(reverse('cart:cart_detail'))

def cart_detail(request):
  cart = Cart(request)
  return render(request,'cart/detail.html',{'cart':cart})


def cart_remove(request,product_id):
  cart = Cart(request)
  product = get_object_or_404(models.Product,id=product_id)
  cart.remove(product)
  return redirect(reverse('cart:cart_detail'))