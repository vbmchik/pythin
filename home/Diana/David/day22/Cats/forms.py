from django import forms

from .models import Price, Breed, Resume, Image
from .catwithimage import CatWithImage

class BreedForm(forms.ModelForm):
   class Meta:
      model= Breed
      fields = ["breed","temperament"]
      labels = {"breed":"Порода", "temperament": "Характер"}

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ["breed","color", "age", "price","image"]
        labels = {"breed": "Порода", "color": "Окрас", "age": "Возраст", "price": "ЦЕНА", "image": "Добавить картинку" }

class ResumeForm(forms.ModelForm):




   class Meta:
      model = Resume
      fields = ['file']
      
      
class ImageForm(forms.ModelForm):

   class Meta:
      model = Image
      fields = ['image']
      
      
      
