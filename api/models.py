from django.db import models

class Country(models.Model):
    place = models.CharField(max_length=20, unique=True)
