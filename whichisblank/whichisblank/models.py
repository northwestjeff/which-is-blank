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
    size_rank = models.IntegerField()
    population_2008 = models.IntegerField()
    land_area_sq_km = models.IntegerField()

    def __str__(self):
        return self.country_name

class Comparison(models.Model):
    user = models.ForeignKey(User, related_name="user_comp_instance", on_delete=models.CASCADE)
    first_comp = models.ForeignKey(Country, related_name="country_a", on_delete=models.CASCADE)
    second_comp = models.ForeignKey(Country, related_name="country_b", on_delete=models.CASCADE)
    vote = models.BooleanField()
    correct = models.BooleanField()




