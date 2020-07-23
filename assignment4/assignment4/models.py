from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    passwd = models.CharField(max_length=100, unique=True)
    phonenumber = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    def _str_(self):
        return self