from django.shortcuts import render
from .models import Name,Color,Cat

# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "catsapps/index.html")

def names(request):
    name = Name.objects.order_by("name")
    content = {"NAME":name}
    return render(request, "catsapps/names.html", content)

def name(request, name_id):
    name = Name.objects.get(id=name_id)
   
    context = { "NAME": name }
    return render(request, "catsapps/name.html", context)


def colors(request):
    color = Color.objects.order_by("color")
    content = {"COLOR":color}
    return render(request, "catsapps/colors.html", content)

def color(request, color_id):
    color = Color.objects.get(id=color_id)
    cats = color.entry_set.order_by("color")
    context = {"COLOR": color, "CATS": cats}
    return render(request, "catsapps/color.html", context)



def cats(request):
    cats = Cat.objects.order_by("name")
    context = {"CATS": cats}
    return render(request, "catsapps/cats.html", context)

def cat(request, cats_id):
    cat = Cat.objects.get(id=cats_id)
    context = {"CAT": cat}
    return render(request, "catsapps/cat.html", context)


