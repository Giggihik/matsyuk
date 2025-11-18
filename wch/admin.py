from django.contrib import admin
from .models import Hotel, RoomType, Room, Guest, Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'address']
    list_filter = ['name']
    search_fields = ['name', 'email']
    list_per_page = 20

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_per_night', 'description_short']
    list_filter = ['price_per_night']
    search_fields = ['name']
    list_editable = ['price_per_night']  
    
    def description_short(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_short.short_description = 'Description'

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'room_type', 'hotel', 'status', 'price_per_night']
    list_filter = ['status', 'room_type', 'hotel']
    search_fields = ['room_number', 'hotel__name']
    list_editable = ['status']
    list_per_page = 25
    
    def price_per_night(self, obj):
        return obj.room_type.price_per_night
    price_per_night.short_description = 'Price/Night'

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'passport_number']
    list_filter = ['last_name']
    search_fields = ['first_name', 'last_name', 'email', 'passport_number']
    list_per_page = 30
    
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Full Name'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'guest_name', 'room_info', 'check_in_date', 'check_out_date', 'status', 'total_amount']
    list_filter = ['status', 'check_in_date', 'check_out_date']
    search_fields = ['guest__first_name', 'guest__last_name', 'room__room_number']
    list_editable = ['status']
    date_hierarchy = 'created_at'
    list_per_page = 25
    
    def guest_name(self, obj):
        return f"{obj.guest.first_name} {obj.guest.last_name}"
    guest_name.short_description = 'Guest'
    
    def room_info(self, obj):
        return f"{obj.room.room_number} ({obj.room.room_type.name})"
    room_info.short_description = 'Room'