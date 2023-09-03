from django.urls import path
from . import views


urlpatterns = [
    path('properties/', views.PropertyList.as_view(), name='property-list'),
    path('properties/<int:property_id>/', views.PropertyDetail.as_view(), name='property-detail'),
]
