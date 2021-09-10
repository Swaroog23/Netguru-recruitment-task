from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100, unique=True)


class CarRating(models.Model):
    rating = models.IntegerField(null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="rating")