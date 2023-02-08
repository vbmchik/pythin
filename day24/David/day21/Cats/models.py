from django.db import models

# Create your models here.


class Temperament(models.Model):
    temperament = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return f"{self.temperament}"
    
class Breed(models.Model):
    breed = models.CharField(max_length=40, unique=True)
    temperament = models.ForeignKey(
        Temperament, on_delete=models.CASCADE, primary_key=False)
    def __str__(self):
        return f"Название породы: {self.breed}, характер: {self.temperament}"

    
class Color(models.Model):
    color = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.color}"
    

class Price(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, primary_key=False)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, primary_key=False)
    age = models.CharField(max_length=3, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, primary_key=False)
        
    date_added = models.DateTimeField(auto_now_add=True, primary_key=False)

    def __str__(self):
        return f"{self.breed} Цвет: {self.color} Возраст: {self.age} ЦЕНА: {self.price}"    