from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Breed(models.Model):
    breed = models.CharField(max_length=40)
    temperament = models.CharField(max_length=40)
    date_added = models.DateTimeField(auto_now_add=True, primary_key=False)
    
    def __str__(self):
        return f"Порода: {self.breed} Характер: {self.temperament}"



class Resume(models.Model):
    file = models.FileField(upload_to= 'Cats',null=True)
    name = models.CharField(max_length= 255, blank=False, null=False)
    def __repr__(self):
        return 'Resume(%s, %s)' % (self.file)

    def __str__ (self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length= 255, blank=False, null=False)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    def __repr__(self):
        return 'Image(%s, %s)' % (self.title, self.image)

    def __str__ (self):
        return self.title

    
class Price(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, primary_key=False) 
    color = models.CharField(max_length= 20)
    age = models.CharField(max_length= 2)
    price = models.DecimalField(decimal_places=2, max_digits=10, primary_key=False)
    date_added = models.DateTimeField(auto_now_add=True, primary_key=False)
    
    def __str__(self):
        return f"Порода: {self.breed} Окрас: {self.color} Возраст: {self.age} ЦЕНА: {self.price}"    
