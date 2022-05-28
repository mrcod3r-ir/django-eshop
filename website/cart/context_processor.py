from .cart import Cart

def cart(request):
  x = Cart(request)
  print('=======================')
  print(x.cart)
  print('=======================')
  return {'cart':Cart(request).cart}