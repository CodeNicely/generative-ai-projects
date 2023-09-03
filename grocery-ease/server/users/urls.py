from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserPasswordUpdateView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('password/', UserPasswordUpdateView.as_view(), name='user-password-update'),
]
