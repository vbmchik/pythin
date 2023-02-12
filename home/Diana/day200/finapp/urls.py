from django.urls import path

from . import views

app_name = "finapp"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("stats/", views.stats, name="finappstats"),
    path("years/", views.yearswithincome, name="ylist"),
    path("months/<str:year>", views.monthswithincome, name="mlist"),
    path("mincomes/<str:year>/<str:month>", views.incomes, name="incs"),
]
