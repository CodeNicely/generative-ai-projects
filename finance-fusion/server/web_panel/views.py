from django.shortcuts import render


def home(request):
    return render(request, 'web_panel/home.html')
