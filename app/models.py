from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, timezone, timedelta
# Create your models here.


class Sender(models.Model):
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    company = models.CharField(max_length=50)


class Courier(models.Model):
    def __str__(self):
        return '{} {} {} {}'.format(self.first_name, self.last_name, self.vehicle_type, self.phone)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)


class Delivery(models.Model):
    def __str__(self):
        return '{} {} {}'.format(self.date, self.description, self.cost)
    courier = models.ForeignKey(
        Courier, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now())
    description = models.CharField(max_length=500, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
