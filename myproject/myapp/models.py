from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    mobile=models.CharField(max_length=12, verbose_name='Contact Number')
    address=models.TextField(verbose_name='Address')

class Doctor(models.Model):
    did=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=255, verbose_name='Doctor name')
    ddegree=models.CharField(max_length=255)