from django.urls import path
from .views import PropertyListCreateView, PropertyRetrieveUpdateDestroyView


urlpatterns = [
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyRetrieveUpdateDestroyView.as_view(), name='property-retrieve-update-destroy'),
]
