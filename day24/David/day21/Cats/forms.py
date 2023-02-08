from django import forms

from .models import Temperament, Breed, Color, Price


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['color']
        labels = {'color': 'Окрас'}

class TempForm(forms.ModelForm):
    class Meta:
        model = Temperament
        fields = ['temperament']
        labels = {'temperament': 'Характер'}
        
class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed # Я застрял
        fields = ['temperament', 'breed']
        labels = {'breed':'Порода', 'temperament':'Характер'}
        #labels = {'breed': 'breed'}
        
class CatForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['breed','color','age','price']
        labels = {'breed':'Порода', 'color':'Окрас','age':'Возраст', 'price': 'Цена'}        