from django.contrib import admin
from .models import Color,Kind,Behavor,Cat

# Register your models here.

admin.site.register(Cat)
admin.site.register(Behavor)
admin.site.register(Kind)
admin.site.register(Color)
