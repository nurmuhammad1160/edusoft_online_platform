from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.views import View



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
    return render(request, 'register/signup.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'register/index.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def profile_view(request):
    return render(request, 'profile/profile.html', {'user': request.user})



class EditProfileView(View):
    def get(self, request):
        form = UserChangeForm(instance=request.user)
        return render(request, 'profile/edit_profile.html', {'form': form})

    def post(self, request):
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'profile/edit_profile.html', {'form': form})