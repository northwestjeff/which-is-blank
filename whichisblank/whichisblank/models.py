from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Author(models.Model):
    author_name = models.CharField(max_length=200)

class Country(models.Model):
    country_name = models.CharField(max_length=200)
    capital_city = models.CharField(max_length=200)
    size_rank = models.IntegerField
    population_2008 = models.IntegerField
    land_area_sq_km = models.IntegerField


