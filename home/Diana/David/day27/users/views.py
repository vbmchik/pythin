from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    if request.method != "POST":
        form= UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid:
            new_user = form.save()
            login(request, new_user) 
            return redirect("Food:index")
    mapper = {"form": form}
    return render(request, "registration/register.html", mapper)


