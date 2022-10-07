from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Users(models.Model):
    #host =
    #topic =
    Username = models.TextField(_MAX_LENGTH=200)(NULL=False)
    UserBdate = models.DateTimeField(NULL=False)
    UserGender = models.CharField(NULL=False)
    UserEmail = models.TextField(_MAX_LENGTH=200)(NULL=False)
    UserMatricula = models.CharField(_MAX_LENGTH=8)(NULL=False)
    UserPassword = models.TextField(_MAX_LENGTH=25)(NULL=False)
    updated = models.DateTimeField(auto_now=True)
    