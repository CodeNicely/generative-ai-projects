from django.shortcuts import render


def home(request):
    return render(request, 'web_panel/home.html')


def register(request):
    return render(request, 'user_management/register.html')


def login(request):
    return render(request, 'user_management/login.html')


def dashboard(request):
    return render(request, 'user_management/dashboard.html')


def profile(request):
    return render(request, 'user_management/profile.html')


def settings(request):
    return render(request, 'user_management/settings.html')
