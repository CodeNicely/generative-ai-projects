from django.urls import path
from .views import home, register, login, dashboard, profile, settings


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('settings/', settings, name='settings'),
]
