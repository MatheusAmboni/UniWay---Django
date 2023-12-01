from django.urls import path
from .views import index, create_user, create_trip, create_ride, create_review, create_car, create_endereco

urlpatterns = [
    path('', index, name='index'),
    path('create-user/', create_user, name='create_user'),
    path('create-trip/', create_trip, name='create_trip'),
    path('create-ride/', create_ride, name='create_ride'),
    path('create-review/', create_review, name='create_review'),
    path('create-car/', create_car, name='create_car'),
    path('create-endereco/', create_endereco, name='create_endereco'),
]
