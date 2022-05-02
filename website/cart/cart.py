from django.conf import settings
from shop import models
class Cart:
  def __init__(self,request):
    self.session = request.session
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
      cart = self.session[settings.CART_SESSION_ID] = {}
    self.cart = cart
    
  def add(self,product,product_count=1,update_count=False):

    product_id = str(product.id)
    if product_id not in self.cart:
      self.cart[product_id] = {'product_count':0,'price':str(product.price)}
      
    if update_count:
      self.cart[product_id]['product_count'] = product_count
    else:
      self.cart[product_id]['product_count'] += product_count
    self.save()
    
  def save(self):
    self.session[settings.CART_SESSION_ID] = self.cart
    self.session.modified = True
    
  def show_cart(self):
    product_ids = self.cart.keys()
    products = models.Product.objects.filter(id__in = product_ids)
    return products
    
    