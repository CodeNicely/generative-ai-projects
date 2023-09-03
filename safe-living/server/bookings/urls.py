from django.urls import path
from . import views


urlpatterns = [
    path('bookings/', views.BookingList.as_view(), name='booking-list'),
    path('bookings/<int:booking_id>/', views.BookingDetail.as_view(), name='booking-detail'),
]
