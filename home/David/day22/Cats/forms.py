from django import forms

from .models import Price, Resume, Image

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ["breed","temperament","color", "age", "price"]
        labels = {"breed": "Порода", "temperament": "Характер", "color": "Окрас", "age": "Возраст", "price": "ЦЕНА"}

class ResumeForm(forms.ModelForm):

   class Meta:
      model = Resume
      fields = ['file']
      
      
class ImageForm(forms.ModelForm):

   class Meta:
      model = Image
      fields = ['image']
      
      
      
