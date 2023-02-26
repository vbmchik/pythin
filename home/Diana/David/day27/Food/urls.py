from django.urls import path


from . import views

app_name = "Food"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    path("jobRestaurant/", views.jobRestaurant, name="JobRestaurant"),
    path("AddRestaurant/", views.AddRestaurant, name="AddRestaurant"),
    path("DelRestaurant/<str:res_id>", views.DelRestaurant, name="DelRestaurant"),
    path("GetPost/<str:res_id>", views.getpost, name="getpost"),
    path("Moderatorpost/", views.PermissionPost, name="moderatorposts"),
    path("updatePost/<str:res_id>", views.updatepost, name="updatepost"),

]

