from django.shortcuts import render, redirect
from .models import User, Trip, Review, Car, Endereco
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm, UserForm, TripForm, ReviewForm, CarForm, EnderecoForm
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

def index(request):
    users = User.objects.all()
    trips = Trip.objects.all()
    reviews = Review.objects.all()
    car = Car.objects.all()
    endereco = Endereco.objects.all()

    context = {
        'users': users,
        'trips': trips,
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


def find_trips(request):
    trips = Trip.objects.all()

    context = {
        'trips': trips,
    }
    return render(request, 'find_trips.html', context)


def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['senha']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def agendar_carona(request, trip_id):
    # Lógica para diminuir o número de assentos
    trip = Trip.objects.get(id=trip_id)
    if request.user.username != trip.passengers:
        trip.available_seats -= 1
    trip.passengers = request.user.username
    trip.save()

    # Responda com um JSON indicando sucesso ou falha
    return JsonResponse({'success': True})

def suasviagens(request):
    trips = Trip.objects.all()

    context = {
        'trips': trips,
    }
    return render(request, 'suasviagens.html', context)

def remove_trip_view(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    
    trip.available_seats += 1
    trip.passengers = ''
    trip.save()

    # Redirecione para a página de viagens do usuário
    return redirect('../../suasviagens')

def pagina_nao_encontrada(request, exception):
    return render(request, '404.html', status=404)