from django.urls import path


from . import views

app_name = "Cats"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    path('upload_resume/',views.upload_resume, name = "files"),
    path('upload_images/',views.upload_images, name = "images" ),
    path("dateCats/", views.all_cat, name="allCats"),
    path("dateCatsbycolor/", views.all_color, name="allColors"),
    path("catindivid/<str:color_name>", views.catsbycolor, name="catbycolor"),
    path("catindividimage/<str:cat_id>/", views.catsbycolor, name="ID"),
    path("addCat/", views.add_cat, name="addCat"),
]
