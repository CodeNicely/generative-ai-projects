from django.urls import path
from .views import MaintenanceRequestListCreateView, MaintenanceRequestRetrieveUpdateDestroyView


urlpatterns = [
    path('maintenance-requests/', MaintenanceRequestListCreateView.as_view(), name='maintenance-request-list-create'),
    path('maintenance-requests/<int:pk>/', MaintenanceRequestRetrieveUpdateDestroyView.as_view(), name='maintenance-request-retrieve-update-destroy'),
]
