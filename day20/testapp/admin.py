from django.contrib import admin
from .models import Color, Brand, Phone
# Register your models here.
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Phone)
