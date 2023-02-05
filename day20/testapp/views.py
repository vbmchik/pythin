from django.shortcuts import render
from .models import Brand, Phone, Color

# Create your views here.

def index(request):
    brands = Brand.objects.order_by("brand")
    mapper = {"Brands": brands}
    return render(request,"testapp/index.html", mapper)

def phonesbybrand(request, brand_id):
    phones = Phone.objects.filter(brand=brand_id)
    mapper = {"FilteredPhones": phones}
    return render(request,"testapp/bphones.html",mapper)

def colors(request):
    colors_id = Phone.objects.values("color").distinct()
    colors = Color.objects.filter(id__in=colors_id).order_by("color")
    mapper = {"Colors": colors}
    return render(request,"testapp/colors.html", mapper)

def phonesbycolor(request, color_id):
    phones = Phone.objects.filter(color=color_id)
    mapper = {"FilteredPhones": phones}
    return render(request, "testapp/bphones.html", mapper)
    