from django.urls import path
from . import views


urlpatterns = [
    path('leases/', views.LeaseList.as_view(), name='lease-list'),
    path('leases/<int:lease_id>/', views.LeaseDetail.as_view(), name='lease-detail'),
]
