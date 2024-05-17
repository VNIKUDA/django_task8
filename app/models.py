from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    genres = models.ManyToManyField("Genre", related_name="games")

class Genre(models.Model):
    title = models.CharField(max_length=200)
