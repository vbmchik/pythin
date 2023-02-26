from django import forms

from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ["categ","restaurant", "characteristic", "city", "street", "image"]
        labels = {"categ": "Категория","restaurant":"Ресторан", "characteristic":"Описание", "city":"Город","street":"Улица", "image":"Лого" }
        
        