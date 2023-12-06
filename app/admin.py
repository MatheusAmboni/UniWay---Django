from django.contrib import admin

from .models import Trip, User, Review, Car, Endereco

admin.site.register(Car)
admin.site.register(Endereco)
admin.site.register(Trip)
admin.site.register(User)
admin.site.register(Review)