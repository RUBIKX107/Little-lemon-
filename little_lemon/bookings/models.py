from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    guests = models.IntegerField()

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)