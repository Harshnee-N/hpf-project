from django.contrib import admin
from .models import Parent, LSAProfile, BookingRequest

admin.site.register(Parent)
admin.site.register(LSAProfile)
admin.site.register(BookingRequest)