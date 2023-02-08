
from django.shortcuts import render, redirect
from .models import Breed, Temperament, Color, Price
from .forms import TempForm, BreedForm, ColorForm, CatForm
from .ColorPlus import ColorPlus



def index(request):
    """Home page of application"""
    return render(request, "Cats/index.html")


def allbreed(request):
    breeds = Breed.objects.all()
    mapper = {"BREED": breeds}
    return render(request, "Cats/allbreed.html", mapper)


def alltemps(request):
    temps = Temperament.objects.all()
    mapper = {"TEMP": temps}
    return render(request, "Cats/alltemp.html", mapper)


def allcolors(request):
    temps = Color.objects.all()
    catsnumbers = []
    for color in temps:
        c = ColorPlus()
        c.color = color
        c.n = Price.objects.filter(color=color.id).count()
        catsnumbers.append(c)
    mapper = {"TEMP": catsnumbers}
    return render(request, "Cats/allcolors.html", mapper)


def catsbycolor(request, color_id):
    listcats = Price.objects.filter(color=color_id)
    mapper = {"LIST": listcats}
    return render(request, "Cats/filteredcats.html", mapper)

def allcats(request):
    listcats = Price.objects.all()
    mapper = {"LIST": listcats}
    return render(request, "Cats/allcats.html", mapper)

def statetemperament(request, breed_id):
    b = Price.objects.filter(breed=breed_id)
    mapper = {"TEMPERAMENTS": b}
    return render(request, "Cats/Temp.html", mapper)


def add_breed(request):
    if request.method != "POST":
        # NO DATE IN REQUEST
        form = BreedForm()
    else:
        form = BreedForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:allbreed")
        
    mapper = {"FORMBREED": form}
    return render(request, "Cats/addBreed.html", mapper)
    

def add_temp(request):
    
    if request.method != "POST":
        # NO DATE IN REQUEST
        form = TempForm()
    else:
        form = TempForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:alltemps")

    mapper= {"FORM": form}
    return render(request, "Cats/addTemp.html", mapper)


def add_color(request):

    if request.method != "POST":
        # NO DATE IN REQUEST
        form = ColorForm()
    else:
        form = ColorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:allcolors")

    mapper = {"FORM": form}
    return render(request, "Cats/addColor.html", mapper)


def add_cat(request):

    if request.method != "POST":
        # NO DATE IN REQUEST
        form = CatForm()
    else:
        form = CatForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:allcats")

    mapper = {"FORM": form}
    return render(request, "Cats/addCat.html", mapper)

