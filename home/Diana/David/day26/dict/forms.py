from django import forms
from .models import Cats, Words

class CatFORM(forms.ModelForm):
    class Meta:
        model = Cats
        fields=["name"]
        labels={"name":"Название категории"}
        
        

    

"""  cat = models.ForeignKey(Cats,on_delete=models.CASCADE)
    word = models.CharField(max_length=15, unique=True)
    transc = models.CharField(max_length=40)
    meaning = models.TextField(max_length=200) """   
    
class WordFORM(forms.ModelForm):
    class Meta:
        model = Words
        fields = ["cat", "word", "transc", "meaning"]
        labels = {"cat":"", "word": "Слово", "transc": "Произношение", "meaning": "Перевод"}
        