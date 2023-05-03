from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductsForm
from cart import cart



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    if (product.stock < 21):
        pquant = int(product.stock+1)
        if( pquant == 1 ):
            cart_product_form = None
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()
    quant = cart.Cart(request).productq(str(id))
    if cart_product_form:
        return render(request,
                    'shop/product/detail.html',
                    {'product': product,
                     'yescart': True,
                     'cart_product_form':cart_product_form})
    else:
        return render(request,
                      'shop/product/detail.html',
                      {'product': product,})
