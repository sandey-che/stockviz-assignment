from django.db import models

class countryGDP(models.Model):
    countryname = models.CharField(max_length=60)
    year = models.CharField(max_length=60)
    gdp = models.CharField(max_length=60)

class GDP(models.Model):
    year = models.CharField(max_length=4)
    India = models.IntegerField(max_length=4)
    USA = models.IntegerField(max_length=4)
    Europe = models.IntegerField(max_length=4)
    China = models.IntegerField(max_length=4)
    