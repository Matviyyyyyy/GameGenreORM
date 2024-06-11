from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=300)
    genre = models.ManyToManyField("Genre")
    year_release = models.IntegerField()
    rating = models.DecimalField(decimal_places=2, max_digits=15)

class Genre(models.Model):
    name = models.CharField(max_length=100)
