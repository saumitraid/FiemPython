from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    mobile=models.CharField(max_length=12, verbose_name='Contact Number')
    address=models.TextField(verbose_name='Address')