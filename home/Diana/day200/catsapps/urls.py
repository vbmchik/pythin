from django.urls import path

from . import views

app_name = "catsapps"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("names/", views.names, name="names"),
    path("name/<int:name_id>", views.name, name="name"),
    path("colors/", views.colors, name="colors"),
    path("color/<int:color_id>", views.color, name="color"),
    path("cats/", views.cats, name="cats"),
    path("cat/<int:cats_id>", views.cat, name="cat"),
]
