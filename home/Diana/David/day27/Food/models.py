from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Category(models.Model):
    categ = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.categ}"


class Restaurant(models.Model):
    categ = models.ForeignKey(Category, on_delete=models.CASCADE) 
    restaurant = models.CharField(max_length=40)
    characteristic= models.TextField()
    city= models.CharField(max_length=30)
    street= models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    approved =models.DecimalField(decimal_places= 2, max_digits =10, default=0, null= True)
    date_added = models.DateTimeField(auto_now_add=True, primary_key=False)
    owner= models.ForeignKey(User, on_delete=models.CASCADE) 
    def __repr__(self):
        return 'Image(%s, %s)' % (self.image)   
    def __str__(self):
        return f"Ресторан: {self.restaurant}; {self.characteristic[:50]}... Город: {self.city}"     






    

