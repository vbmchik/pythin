from django.urls import path

from . import views

app_name = "catsapps"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("kind/", views.kind, name="kinds"),
    path("kindbycats/<int:kind_id>", views.kindbycats, name="kind"), 
    
    path("behavor/", views.behavor, name="behavors"),
    path("behavorbycats/<int:behavor_id>", views.behavorbycats, name="behavor"), 
    
    path("color/", views.color, name="colors"),
    path("colorbycats/<int:color_id>", views.colorbycats, name="color"), 
    
    path("cats/", views.cats, name="cats"),
    path("catss/<int:catss_id>", views.catss, name="cats"), 
    
     path("addCats/", views.add_cats, name="addCats"),
    
    
    
]
 # "name/"- просто ссылка, views должен совпадать с нашей созданной функцией в ней, name="names"- как мы будем обращаться по ссылке в html