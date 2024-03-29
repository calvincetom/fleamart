from decimal import Decimal
from django.conf import settings
from Main.models import Product

class Cart:
    def __init__(self,request):
        '''
        initialize the cart

        '''
        self.session = request.session
        cart = self.session.get("settings.CART_SESSION_ID")
        if not cart:
            '''save the empty cart in the session'''
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    #method to add products to the cart or update their quantity
    def add(self, product, quantity=1, override_quantity=False):
        '''Add a product to the cart or update its quantity'''
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        '''mark the session as "modified" to make sure it gets saved'''
        self.session.modified = True