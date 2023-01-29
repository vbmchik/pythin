from django.db import models

# Create your models here.
class Brand(models.Model):
    brand = models.CharField(max_length=15)
    def __str__(self) -> str:
        return f'{self.brand}'
    
class Color(models.Model):
    color = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f'{self.color}'
    
class Phone(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    phone = models.CharField(max_length=45)
    def __str__(self) -> str:
        return f'{self.brand} {self.phone}({self.color})'
