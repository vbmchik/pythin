from django.contrib import admin
from .models import Breed, Price, Resume, Image
# Register your models here.


admin.site.register(Breed)
admin.site.register(Price)
admin.site.register(Resume)
admin.site.register(Image)

from django.contrib.admin.models import LogEntry

#LogEntry.objects.all().delete()