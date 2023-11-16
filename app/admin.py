from django.contrib import admin

from .models import Trip, Ride, User, Review

admin.site.register(Trip)
admin.site.register(Ride)
admin.site.register(User)
admin.site.register(Review)