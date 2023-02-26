from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cats, Words
from .forms import CatFORM, WordFORM
from django.http import Http404
# Create your views here.

def index(request):
    return render(request, "dict/index.html")

@login_required
def cats(request):
    cats = Cats.objects.filter(author=request.user.id).order_by("name")
    mapper = {"cats": cats}
    return render(request,"dict/cats.html",mapper)

def addcat(request):
    if request.method != 'POST':
        form = CatFORM()
    else:
        form = CatFORM(data=request.POST)

        if form.is_valid:
            new_cat = form.save(commit=False)
            new_cat.author = request.user
            new_cat.save()
            return redirect('dict:cats')
    context = {'form': form}
    return render(request, 'dict/newcat.html', context)

def words(request):
    words = Words.objects.filter(author=request.user.id).order_by("word")
    mapper = {"words": words}
    return render(request,"dict/words.html",mapper)


def addword(request):
    if request.method != 'POST':
        form = WordFORM()
    else:
        form = WordFORM(data=request.POST)

        if form.is_valid:
            new_word = form.save(commit=False)
            new_word.author = request.user
            new_word.save()
            return redirect('dict:words')
    context = {'form': form}
    return render(request, 'dict/newword.html', context)

def train(request):
    words = Words.objects.filter(author=request.user.id).order_by("?")[0:3]
    mapper = {"words": words}
    return render(request,"dict/train.html",mapper)


def updatecat(request, cat_id):
    categ = Cats.objects.get(id=cat_id)
    cats = Cats.objects.filter(author=request.user.id)
    if categ.author != request.user:
        raise Http404
    if request.method != 'POST':
        # Current record state
        form = CatFORM(instance=categ)
    else:
        form = CatFORM(instance=categ, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dict:cats')
        
    mapper = {"Form": form, "cats":cats}
    
    return render(request,'dict/update_cat.html', mapper )
    
    