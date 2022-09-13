from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Usuario(models.Model):
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    totalReports = models.IntegerField()
    pswd = models.CharField(max_length=50)


class Cai(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    class Meta:
        db_table = "Cai"
