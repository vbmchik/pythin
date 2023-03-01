from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != 'POST':
        form = UserCreationForm
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid:
            new_user = form.save()
            login(request, new_user)
            return redirect('catsapps:index')
    context = {'form':form}
    return render(request, 'registration/register.html', context)