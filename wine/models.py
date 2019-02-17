from django.db import models

# Create your models here.
from django.db import models


class wine(models.Model):
    id = models.BigIntegerField(unique = True,primary_key= True, null= False)
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    designation = models.CharField(max_length=70)
    points = models.IntegerField()
    price = models.FloatField()
    province = models.CharField(max_length=100)
    region1 = models.CharField(max_length=100)
    region2 = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    winery = models.CharField(max_length=100)

