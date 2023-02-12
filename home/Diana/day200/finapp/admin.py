from django.contrib import admin
from .models import Year, Month, Business, Incomes

# Register your models here.
admin.site.register(Year)
# admin.site.register(Month)
admin.site.register(Business)
admin.site.register(Incomes)
