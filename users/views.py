from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:home')
    else:
        form = UserCreationForm()
    return render(request, 'users/registration/register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('shop:home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/registration/login.html', {'form':form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('shop:home')