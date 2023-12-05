from django import forms
from .models import Endereco, User, Car, Trip, Ride, Review

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'cidade', 'estado']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_passenger', 'username', 'idade', 'email', 'senha', 'endereco']

class LoginForm(forms.Form):
    is_passenger = forms.BooleanField()
    username = forms.CharField()
    idade = forms.IntegerField()
    email = forms.EmailField()
    senha = forms.CharField()
    endereco = forms.CharField()

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['placa', 'cor', 'usuario']

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
