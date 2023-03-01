from django import forms
from .models import Color, Cat,Behavor,Kind

class KindForm(forms.ModelForm):
    class Meta:
        model = Kind
        fields = ['kind']
        labels = {'kind': 'Gen'}
        
        
class BehavorForm(forms.ModelForm):
    class Meta:
        model = Behavor
        fields = ['behavor']
        labels = {'behavor': 'Comportament'}
        
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ["color"]
        labels = {"Color": "Culoare"}
                      
class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ["color",'behavor','kind']
        labels = {"color": "Culoare",'behavor':'Comportament','kind':'Gen'}
        
