from wch import views
from django.urls import path

urlpatterns = [
    path('', views.root),
    path('booking', views.bookings),
    path('stays', views.stays),
    path('dining', views.dinings),
    path('aquaventure', views.aquaventure)
]
