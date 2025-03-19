from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm


def home_page(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Avtomatik login qilish
            return redirect('home')  # Asosiy sahifaga yuborish
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('login')
