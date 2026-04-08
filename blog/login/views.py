from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def add_user(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/')
    else: 
        form = UserForm()
        return render(request, "add_user.html", {'form': form})

# Create your views here.
