from django.urls import path
from .views import index, create_user, create_trip, create_ride, create_review

urlpatterns = [
    path('', index, name='index'),
    path('create-user/', create_user, name='create_user'),
    path('create-trip/', create_trip, name='create_trip'),
    path('create-ride/', create_ride, name='create_ride'),
    path('create-review/', create_review, name='create_review'),
]
