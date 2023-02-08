from django.urls import path


from . import views

app_name = "Cats"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    path("breed/", views.allbreed, name="allbreed"),
    path("temp/", views.alltemps, name="alltemps"),
    path("color/", views.allcolors, name="allcolors"),
    path("bycolor/<int:color_id>", views.catsbycolor, name="catsbycolor"),
    path("addTemp/", views.add_temp, name="addTemp"),
    path("addBreed/", views.add_breed, name="addBreed"),
    path("addColor/", views.add_color, name="addColor"),
    path("cats/", views.allcats, name="allcats"),
    path("addCat/", views.add_cat, name="addCat"),
]
