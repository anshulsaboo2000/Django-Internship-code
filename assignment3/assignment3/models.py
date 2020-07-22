from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=13)
    address = models.CharField(max_length=500)

    class Meta:
        db_table: 'userdatabasetable'