from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255) #album name
    amount = models.IntegerField() #amount of versions
    artist = models.CharField(max_length=50) 
    release_date = models.DateField(auto_now_add=True)
    description = models.TextField()