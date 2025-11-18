from django.shortcuts import render, redirect
from .models import Hotel, RoomType, Room, Booking, Guest
from django.contrib import messages
from django.utils import timezone

def root(request):
    hotel = Hotel.objects.first()  
    room_types = RoomType.objects.all()[:2]  
    
    return render(request, 'full.html', {
        'hotel': hotel,           
        'room_types': room_types  
    })
def bookings(request):
    room_types = RoomType.objects.all()
    available_rooms = Room.objects.filter(status='available')
    
    if request.method == 'POST':
        try:
            guest = Guest.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                phone_number=request.POST['phone'],
                passport_number=request.POST['passport']
            )
            booking = Booking.objects.create(
                guest=guest,
                check_in_date=request.POST['check_in'],
                check_out_date=request.POST['check_out'],
                number_of_guests=request.POST.get('adults', 1),
                status='pending'
            )
            
            messages.success(request, 'Бронирование успешно создано!')
            return redirect('booking_success', booking_id=booking.id)
            
        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')
    
    return render(request, 'booking.html', {
        'room_types': room_types,
        'available_rooms': available_rooms
    })

def booking_success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking_success.html', {
        'booking': booking
    })


def stays(request):
    room_types = RoomType.objects.all()
    return render(request, 'stays.html', {
        'room_types': room_types
    })

def dinings(request):
    return render(request, 'dining.html')

def aquaventure(request):
    return render(request, 'aquaventure.html')

def booking_success(request):
    return render(request, 'booking_success.html')