from django.urls import path
from .views import index, create_user, create_trip, create_ride, find_rides, create_review, create_car, create_endereco, sobre_nos, sign_in
from django.contrib.auth import views as auth

urlpatterns = [
    path('', index, name='index'),
    path('createuser/', create_user, name='create_user'),

    path('create_trip/', create_trip, name='create_trip'),

    path('createride/', create_ride, name='create_ride'),
    path('createreview/', create_review, name='create_review'),
    path('createcar/', create_car, name='create_car'),
    path('createendereco/', create_endereco, name='create_endereco'),
    path('find_rides/', find_rides, name='find_rides'),
    path('login/', sign_in, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('sobrenos/', sobre_nos, name='sobre_nos'),
]
