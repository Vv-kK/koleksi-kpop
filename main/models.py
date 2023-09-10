from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    artist = models.CharField(max_length=50)
    date_bought = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()