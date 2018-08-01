from django.db import models

# Create your models here.
length = 64
class Flight(models.Model):
    origin = models.CharField(max_length=length )
    destinations = models.CharField(max_length=length)
    duration = models.CharField(max_length=length)
    pass
