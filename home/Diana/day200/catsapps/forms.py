from django import forms
from .models import Color, Cat,Behavor,Kind

class KindForm(forms.ModelForm):
    class Meta:
        model = Kind
        fields = ['kind']
        labels = {'kind': ''}
        
class BrhavorForm(forms.ModelForm):
    class Meta:
        model = Behavor
        fields = ['behavor']
        labels = {'behavor': ''}
        
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ["color"]
        labels = {"Color": ""}
                      
class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ["color",'behavor','kind']
        labels = {"color": "color",'behavor':'behavor','kind':'kind'}
        
