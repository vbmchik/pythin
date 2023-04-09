from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    # HomePage
    path("product/", views.product_list, name='product_list')
 
]
