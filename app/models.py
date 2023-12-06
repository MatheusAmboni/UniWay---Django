from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.rua}, {self.cidade}, {self.estado}" 

class User(models.Model):
    is_passenger = models.BooleanField()
    username = models.CharField(max_length=100)
    idade = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

class Car(models.Model):
    placa = models.CharField(max_length=20)
    cor = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Trip(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    departure_location = models.ForeignKey(Endereco, related_name="trips_departure", on_delete=models.CASCADE)
    destination = models.ForeignKey(Endereco, related_name="trips_destination", on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    available_seats = models.IntegerField()

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_received")
    rating = models.PositiveIntegerField()
    comment = models.TextField()
