from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    ...


class Phone(models.Model):
    full_name = models.CharField(max_length=225)
    decrypt = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Homepage(models.Model):
    full_name = models.CharField(max_length=225)
    decrypt = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Aboutpage(models.Model):
    full_name = models.CharField(max_length=20)
    decrypt = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.full_name


class conatact_us(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email





