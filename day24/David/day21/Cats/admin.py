from django.contrib import admin
from .models import Breed, Temperament, Color, Price
# Register your models here.

admin.site.register(Breed)
admin.site.register(Temperament)
admin.site.register(Color)
admin.site.register(Price)