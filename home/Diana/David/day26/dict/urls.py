from django.urls import path

from . import views

app_name = 'dict'

urlpatterns = [
    #HomePage
    path('', views.index, name='index'),
    path('cats', views.cats, name="cats"),
    path('addcat', views.addcat, name="addcat"),
    path('addcat', views.addcat, name="addcat"),
    path('updatecat<str:cat_id>', views.updatecat, name="updatecat"),
    
    path('words', views.words, name="words"),
    path('addword', views.addword, name="addword"),
    path('train', views.train, name="train"),
]
