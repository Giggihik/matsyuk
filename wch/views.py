from django.shortcuts import render

# Create your views here.
def root(request):
    return render(request, 'full.html')


def bookings(request):
    return render(request, 'booking.html')

def stays(request):
    return render(request, 'stays.html')

def dinings(request):
    return render(request, 'dining.html')

def aquaventure(request):
    return render(request, 'aquaventure.html')