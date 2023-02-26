from django.shortcuts import render, redirect
from .models import Price, Image
from .forms import PriceForm, ResumeForm, ImageForm
from .ColorsPlus import ColorPlus
from .urlsPlus import urlsPlus
from .catwithimage import CatWithImage
from django.contrib.auth.decorators import login_required
from itertools import groupby
from django.db.models import Count
from django.http import Http404
from django.http import HttpResponseRedirect

# Create your views here.


 
def redirect_blog(request):
    return redirect("users:login")


def index(request):
    """Home page of application"""
    return render(request, "Cats/index.html")


@login_required
def all_cat(request): 
    
    Imagesbycat = []
    cats_images = Price.objects.filter(owner=request.user, approved=1)    
    for image in cats_images:
        
        cwi = CatWithImage()          
        cwi.cat = Price.objects.filter(owner=request.user).get(id=image.id)
        cwi.image = "/media/"+image.image.path
        cwi.image = cwi.image.replace(
            "media//Users/vbm/vscode/python/home/David/day22/","")
        
        if cwi.cat.approved == 1:
            Imagesbycat.append(cwi)
        
            
    mapper = {"images": Imagesbycat}
    return render(request,"Cats/allcats.html", mapper)

@login_required
def catsbycolor(request, color_name):
    catsbycolors= Price.objects.filter(owner=request.user,color=color_name)
    cat =[]
    
    for cats in catsbycolors:
        cwi= CatWithImage()
        cwi.cat = Price.objects.filter(owner=request.user).get(id=cats.id)
        cwi.image = "/media/"+cats.image.path
        cwi.image = cwi.image.replace(
            "media//Users/vbm/vscode/python/home/David/day22/", "")
        cat.append(cwi)
    
    
    mapper = {"LISTBYCOLOR": cat}
    return render(request, "Cats/catsbycolor.html" ,mapper)
    
    

    
@login_required    
def all_color(request):
    colors = Price.objects.values("color").distinct()
    catnumber =[]
    for color in colors:
        c = ColorPlus()
        
        c.color = color["color"] # Список цветов
        c.text = "<---Посмотреть--->"
        c.n = Price.objects.filter(owner=request.user,color=c.color).count()
        c.notext =""
        catnumber.append(c)
    
    mapper = {"COLORS": catnumber}
    return render(request,"Cats/allcolors.html", mapper)


@login_required
def add_cat(request):
    
    if request.method != "POST":
        catform = PriceForm()
    else:
        catform = PriceForm(request.POST,  request.FILES)
        
        if catform.is_valid():
            cat = catform.save(commit=False)
            cat.owner = request.user
            cat.save()
            
            catform.save()
            return redirect("Cats:allCats")
    mapper = {"catform": catform}
    return render(request, "Cats/add_Cat.html", mapper)
        
@login_required
def del_cat(request,cat_id):
    cat = Price.objects.get(id=cat_id)
    cat.delete()
    return render(request, "Cats/del_Cat.html")

@login_required        
def PermissionCatsPost(request):
    if not request.user.is_staff:
        raise Http404
    post = []
    cats= Price.objects.filter(approved=0)
    
    for postscats in cats:
        cwi = CatWithImage()          
        cwi.cat = Price.objects.all().get(id=postscats.id)
        cwi.image = "/media/"+postscats.image.path
        cwi.image = cwi.image.replace(
            "media//Users/vbm/vscode/python/home/David/day22/", "")
        post.append(cwi)
        
    mapper = {"postcats": post}
    return render(request,"Cats/postcats.html", mapper)


@login_required
def updatepost(request, cat_id):
    cat = Price.objects.get(id=cat_id)
    cat.approved= 1
    cat.save()
               
    return render(request,"Cats/getdate.html")
    
