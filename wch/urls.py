from wch import views
from django.urls import path

urlpatterns = [
    path('', views.root, name='home'),
    path('booking/', views.bookings, name='bookings'),
    path('stays/', views.stays, name='stays'),
    path('dining/', views.dinings, name='dining'),
    path('aquaventure/', views.aquaventure, name='aquaventure'),
    path('booking/success/', views.booking_success, name='booking_success'),
]
