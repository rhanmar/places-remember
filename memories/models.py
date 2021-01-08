from django.db import models
from django.contrib.auth.models import User


class Point(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # широта
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # долгота

    def __str__(self):
        return f"{str(self.latitude)}, {str(self.longitude)}"


class Place(models.Model):
    name = models.CharField(max_length=80, blank='False', null='False')
    point = models.ForeignKey(Point, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.author}, {self.comment}"
