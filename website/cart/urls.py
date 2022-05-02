from . import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/',views.cart_add,name='cart_add')
]
