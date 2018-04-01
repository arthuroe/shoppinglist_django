from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm


def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        password2 = form.cleaned_data['password2']
        if password != password2:
            return render(request, 'accounts/register.html', {'error_message': 'Passwords do not match'}, {'form': form})
        else:
            user.set_password(password)
            user.save()
            return render(request, 'accounts/login.html', user)
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    logout(request)
    form = UserLoginForm(request.POST or None)
    return render(request, 'accounts/login.html', {'form': form})
