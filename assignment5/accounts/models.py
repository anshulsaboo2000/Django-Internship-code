from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserCreate(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField

    class Meta:
        pass