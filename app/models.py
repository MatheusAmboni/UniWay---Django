from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    # is_passenger = models.BooleanField()

class Trip(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    departure_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    available_seats = models.IntegerField()

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rides_as_driver")
    passengers = models.ManyToManyField(User, related_name="rides_as_passenger")
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_received")
    rating = models.PositiveIntegerField()
    comment = models.TextField()