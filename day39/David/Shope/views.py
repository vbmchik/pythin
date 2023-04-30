from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductsForm
from cart.cart import Cart
# Create your views here.
# сделать функцию для выдачи позиций (позиция позиции и так далее далее) в списке продуктов вывести количества и добавление в корзину
    

def product_list(request, category_slug= None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available= True)
    
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category=category)
    return render(request,
                  "Shope/product/list.html",
                  {
                      "CategorY": category,
                      "CategorieS": categories,
                      "ProductS": products
                  }
                  )
    
def product_details(request, id , slug):
    product = get_object_or_404(Product, id=id, slug= slug, available = True)
    cart_product_form = CartAddProductsForm()

    
    return render(request, 
                  "Shope/product/detail.html",{"ProductS": product, "cart_product_form":cart_product_form})