from django.urls import path
from . import views


urlpatterns = [
    path('maintenance-requests/', views.MaintenanceRequestList.as_view(), name='maintenance-request-list'),
    path('maintenance-requests/<int:maintenance_request_id>/', views.MaintenanceRequestDetail.as_view(), name='maintenance-request-detail'),
]
