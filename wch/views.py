from django.shortcuts import render

# Create your views here.
def root(request):
    return render(request, 'full.html')


def bookings(request):
    return render(request, 'booking.html')