from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Color,Cat,Behavor,Kind
from .forms import CatForm
# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "catsapps/index.html")

@login_required
def kind(request):
    kind = Kind.objects.all()
    content = {"KIND":kind}
    return render(request, "catsapps/kind.html", content)

def kindbycats(request, kind_id):
    kind = Kind.objects.filter(id=kind_id)
    context = { "KINDBYCATS": kind}
    return render(request, "catsapps/kindbycats.html", context) 

def behavor(request):
    behavor = Behavor.objects.all()
    content = {"BEHAVOR":behavor}
    return render(request, "catsapps/behavor.html", content)

def behavorbycats(request, behavor_id):
    behavor= Behavor.objects.filter(id=behavor_id)
    context = { "BEHAVORBYCATS": behavor}
    return render(request, "catsapps/behavorbycats.html", context) 


def color(request):
    color = Color.objects.all()
    content = {"COLOR":color}
    return render(request, "catsapps/color.html", content)

def colorbycats(request, color_id):
    color = Color.objects.filter(id=color_id)
    context = { "COLORBYCATS": color}
    return render(request, "catsapps/colorbycats.html", context) 

def cats(request):
    cats = Cat.objects.all()
    context = {"CATS": cats}
    return render(request, "catsapps/cats.html", context)

def catss(request, cats_id):
    catss = Cat.objects.filter(id=cats_id)
    context = { "CATSS": catss}
    return render(request, "catsapps/catss.html", context) 


def add_cats(request):

    if request.method != "POST":
        # NO DATE IN REQUEST
        form = CatForm()
    else:
        form = CatForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("catsapps:cats")

    mapper = {"FORM": form}
    return render(request, "catsapps/addCats.html", mapper)

