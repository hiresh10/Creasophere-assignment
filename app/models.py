from django.db import models

# Create your models here.
class User(models.Model):
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=100)

class UserMaster(models.Model):
    phone_number = models.CharField(max_length=12)
    name = models.CharField(max_length=50)

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    