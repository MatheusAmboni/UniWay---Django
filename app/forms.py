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

    def __init__(self, *args, **kwargs):
        super(RideForm, self).__init__(*args, **kwargs)
        self.fields['passengers'].queryset = User.objects.filter(is_passenger=True)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'reviewed_user', 'rating', 'comment']
