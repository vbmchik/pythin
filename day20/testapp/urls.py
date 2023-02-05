from django.urls import path

from . import views

app_name = 'testapp'

urlpatterns = [
    # HomePage
    path('', views.index, name='index'),
    path("bphones/<str:brand_id>", views.phonesbybrand, name="bphones"),
    path("colors/",views.colors,name="colors"),
    path("cphones/<str:color_id>", views.phonesbycolor, name="cphones")
]
