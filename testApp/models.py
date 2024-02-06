from django.db import models

# Create your models here.
class Movie(models.Model):

    rDate = models.DateField()
    movieName = models.CharField(max_length = 30)
    hero = models.CharField(max_length = 30)
    heroin = models.CharField(max_length = 30)
    rating = models.CharField(max_length = 30)

