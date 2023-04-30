from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_POST
from Shope.models import Product
from .cart import Cart
from .forms import CartAddProductsForm

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductsForm(request.POST)
    if form.is_valid(): 
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'], override_quantity=cd['override'])
         
    return redirect("cart:cart_detail")
    

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id= product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")

def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})
    
    