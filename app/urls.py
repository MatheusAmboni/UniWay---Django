from django.urls import path
from .views import index, create_user, user_login, create_trip, find_trips, create_review, create_car, create_endereco, sobre_nos, agendar_carona, suasviagens, remove_trip_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('', index, name='index'),

    path('suasviagens/', suasviagens, name='suasviagens'),

    path('createuser/', create_user, name='create_user'),

    path('create_trip/', create_trip, name='create_trip'),

    path('createreview/', create_review, name='create_review'),
    
    path('createcar/', create_car, name='create_car'),

    path('createendereco/', create_endereco, name='create_endereco'),
    
    path('find_trips/', find_trips, name='find_trips'),

    path('login/', user_login, name='login'),

    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),

    path('sobrenos/', sobre_nos, name='sobre_nos'),

    path('agendar_carona/<int:trip_id>/', agendar_carona, name='agendar_carona'),

    path('remove_trip/<int:trip_id>/', remove_trip_view, name='remove_trip'),
]
