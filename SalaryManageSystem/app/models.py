from django.db import models
# Create your models here.
from django.db import models
class People(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=20, null=False)
    sex = models.CharField(max_length=16, null=False)
    year = models.IntegerField(max_length=16, null=False)
    job = models.CharField(max_length=16, null=False)

class salasy(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=20, null=False)
    sex = models.CharField(max_length=20, null=False)
    salasy = models.FloatField(max_length=20, null=False)
    Bonus = models.FloatField(max_length=20, null=False)
    fakuan = models.FloatField(max_length=20, null=False)
    Overtime_pay = models.FloatField(max_length=20, null=False)
