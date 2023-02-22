from django.db import models

# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=100)
   
    def __str__(self) -> str:
        return f"{self.color}"
    
class Behavor(models.Model):
    behavor = models.CharField(max_length=400)

    def __str__(self) -> str:
        return f"{self.behavor}" 
      

class Kind(models.Model):
    kind = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return f"{self.kind}" 
    

class Cat(models.Model):
    color= models.ForeignKey(Color, on_delete=models.CASCADE)
    behavor= models.ForeignKey(Behavor, on_delete=models.CASCADE)
    kind= models.ForeignKey(Kind, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    


    def __str__(self) -> str:
        return f" Color: {self.color}, Behavior: {self.behavor},Kind: {self.kind}"
    


