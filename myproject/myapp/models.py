from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    mobile=models.CharField(max_length=12, verbose_name='Contact Number')
    address=models.TextField(verbose_name='Address')

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=50, verbose_name='Category Name')
    
    def __str__(self):
        return self.cat_name


class Product(models.Model):
    p_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    cat=models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category Name')

class Doctor(models.Model):
    did=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=255, verbose_name='Doctor name')
    ddegree=models.CharField(max_length=255)