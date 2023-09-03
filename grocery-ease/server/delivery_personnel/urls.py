from django.urls import path
from .views import DeliveryPersonnelListView, DeliveryPersonnelDetailView


urlpatterns = [
    path('', DeliveryPersonnelListView.as_view(), name='delivery-personnel-list'),
    path('<int:pk>/', DeliveryPersonnelDetailView.as_view(), name='delivery-personnel-detail'),
]
