from django.shortcuts import render, redirect
from .models import User, Trip, Ride, Review, Car, Endereco
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm, UserForm, TripForm, RideForm, ReviewForm, CarForm, EnderecoForm

def index(request):
    users = User.objects.all()
    trips = Trip.objects.all()
    rides = Ride.objects.all()
    reviews = Review.objects.all()
    car = Car.objects.all()
    endereco = Endereco.objects.all()

    context = {
        'users': users,
        'trips': trips,
        'rides': rides,
        'reviews': reviews,
        'car': car,
        'endereco': endereco,
    }
    return render(request, 'index.html', context)

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('index')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'create_user.html', context)

def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save()
            messages.success(request, 'Viagem criada com sucesso!')
            return redirect('index')
    else:
        form = TripForm()
    context = {'form': form}
    return render(request, 'create_trip.html', context)

def create_ride(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)

    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.trip = trip
            ride.save()
            messages.success(request, 'Carona criada com sucesso!')
            return redirect('index')
    else:
        form = RideForm()
    context = {'form': form, 'trip': trip}
    return render(request, 'create_ride.html', context)

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Avaliação criada com sucesso!')
            return redirect('index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'create_review.html', context)

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            messages.success(request, 'Carro criado com sucesso!')
            return redirect('index')
    else:
        form = CarForm()
    context = {'form': form}
    return render(request, 'create_car.html', context)

def create_endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save()
            messages.success(request, 'Endereço criado com sucesso!')
            return redirect('index')
    else:
        form = EnderecoForm()
    context = {'form': form}
    return render(request, 'create_endereco.html', context)


def find_rides(request):
    trips = Trip.objects.all()
    rides = Ride.objects.all()

    context = {
        'trips': trips,
        'rides': rides,
    }
    return render(request, 'find_rides.html', context)


def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['senha']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = LoginForm()
    return render(request, 'login.html', {'form':form})