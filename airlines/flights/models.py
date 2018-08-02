from django.db import models

# Create your models here.
length = 64

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    # name = models.CharField(max_length=length)

    def __str__(self):
        return f"{self.city} ({self.code}) "

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") # If I access Airport, I can call departures directly without handling the relation myself.
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"        
    
