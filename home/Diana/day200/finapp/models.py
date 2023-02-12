from django.db import models

# Create your models here.
class Year(models.Model):
    year = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.year}"

class Month(models.Model):
    month = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.month}"

class Business(models.Model):
    business = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.business}"

class Incomes(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, primary_key=False)
    month = models.ForeignKey(Month, on_delete=models.CASCADE, primary_key=False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, primary_key=False)
    income = models.DecimalField(decimal_places=2, max_digits=10, primary_key=False)
    date_added = models.DateTimeField(auto_now_add=True, primary_key=False)

    def __str__(self):
        return f"{self.year} {self.month} {self.business}  : {self.income}"
