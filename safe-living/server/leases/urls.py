from django.urls import path
from .views import LeaseListCreateView, LeaseRetrieveUpdateDestroyView


urlpatterns = [
    path('leases/', LeaseListCreateView.as_view(), name='lease-list-create'),
    path('leases/<int:pk>/', LeaseRetrieveUpdateDestroyView.as_view(), name='lease-retrieve-update-destroy'),
]
