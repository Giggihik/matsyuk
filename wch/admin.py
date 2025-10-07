from django.contrib import admin
from .models import *

admin.site.register(Hotel)
admin.site.register(Room_type)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Booking)