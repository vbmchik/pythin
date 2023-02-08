from django.urls import path


from . import views

app_name = "Cats"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    path("breed/", views.allbreed, name="allbreed"),
    path("temperament/<str:breed_id>", views.statetemperament, name="statetemperament"),
    path("addTemp/", views.add_temp, name="addTemp"),
    path("addBreed/", views.add_breed, name="addBreed"),
]
