from django.db import models

# Create your models here.
class Accounts(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=25)
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)