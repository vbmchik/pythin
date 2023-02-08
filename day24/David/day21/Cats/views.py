
from django.shortcuts import render, redirect
from .models import Breed, Temperament, Color, Price
from .forms import TempForm, BreedForm



def index(request):
    """Home page of application"""
    return render(request, "Cats/index.html")


def allbreed(request):
    breeds = Breed.objects.all()
    mapper = {"BREED": breeds}
    return render(request, "Cats/allbreed.html", mapper)


def allbreed(request):
    temps = Temperament.objects.all()
    mapper = {"BREED": temps}
    return render(request, "Cats/alltemps.html", mapper)


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
            return redirect("Cats:statetemperament")

    mapper= {"FORM": form}
    return render(request, "Cats/addTemp.html", mapper)

