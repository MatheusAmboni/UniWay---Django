from django import forms
from .models import Trip, User, Ride, Review

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['driver', 'departure_location', 'destination', 'date_time', 'available_seats']

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['driver', 'passengers', 'start_location', 'end_location']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'reviewed_user', 'rating', 'comment']
