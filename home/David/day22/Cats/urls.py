from django.urls import path


from . import views

app_name = "Cats"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    
    
    path("deletecats/<str:cat_id>", views.del_cat, name="delCat"),
    path("updatepost/<str:cat_id>", views.updatepost, name="updatepost"),
    path("PermissionCatPost/", views.PermissionCatsPost, name="PermissionCatsPost"),
    path("dateCats/", views.all_cat, name="allCats"),
    path("dateCatsbycolor/", views.all_color, name="allColors"),    
    path("catindivid/<str:color_name>", views.catsbycolor, name="catbycolor"),
    path("addCat/", views.add_cat, name="addCat"),
]
