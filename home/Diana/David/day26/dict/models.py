from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Здесь определяем категории для словаря
class Cats(models.Model):
    name = models.CharField(max_length=15, unique=True)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Words(models.Model):
    cat = models.ForeignKey(Cats,on_delete=models.CASCADE)
    word = models.CharField(max_length=15, unique=True)
    transc = models.CharField(max_length=40)
    meaning = models.TextField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.word} : {self.meaning}'
