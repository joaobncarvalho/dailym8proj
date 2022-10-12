from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class User(models.Model):
    #host =
    #topic =
    Username = models.CharField(max_length=200, null=False)
    UserBdate = models.DateTimeField(null=False),
    UserGender = models.CharField(null=False),
    UserEmail = models.CharField(max_length=200, null=False)
    UserMatricula = models.CharField(max_length=8, null=False)
    UserPassword = models.CharField(max_length=25, null=False)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.Username