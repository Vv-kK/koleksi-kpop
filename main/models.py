from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255) #album name
    amount = models.IntegerField() #amount of versions
    artist = models.CharField(max_length=50) 
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)