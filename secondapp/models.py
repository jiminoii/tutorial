from django.db import models

# Create your models here.
class Hospital(models.Model):
    sido = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    medical = models.CharField(max_length=255)
    tel= models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

