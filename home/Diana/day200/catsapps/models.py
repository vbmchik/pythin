from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=15)
    data_added = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"
    
class Color(models.Model):
    color = models.CharField(max_length=15)
    data_added = models.DateField(auto_now_add=True)
    def __str__(self) :
        return f"{self.color}"

class Cat(models.Model):
    name= models.ForeignKey(Name, on_delete=models.CASCADE)
    color= models.ForeignKey(Color, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "cats"

    def __str__(self) -> str:
        return f"{self.name}{self.cats}{self.color}"
    


