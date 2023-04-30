from decimal import Decimal
from django.conf import settings
from Shope.models import Product

class Cart:
    def __init__(self, request):
        self.session= request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]= {}
        self.cart = cart
    
    def pozition(self):
        cart_len = len(self.cart.keys())
        if cart_len > 0:
            text = f"Ваша корзина: "
            if cart_len == 1:
                text += f" {cart_len} Позиция"
            elif cart_len < 5:
                text += f" {cart_len} Позиции"
            else:
                text += f" {cart_len} Позиций"
        
        return text + f" на сумму {self.get_total_price()} NIS"

    def add(self, product, quantity=1, override_quantity= False):
        product_id = int(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": int(product.price)
            }
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()
    
    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def save(self):
        self.session.modified= True
        
        
    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        cart= self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"]= product
            
            
        for item in cart.values():
            item["price"] = Decimal(item["price"]) # Сумма товара  
            item["total_price"] = item["price"]*item["quantity"] # Сумма всех товаров определенного типа

            yield item    
        
    
    def __len__(self):
        return sum(item["quantity"] for _,item in self.cart.items() ) # Считаем всю корзину!
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
    
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID] # Удаляем  сессию!
            
        