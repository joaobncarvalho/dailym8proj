from asyncio.windows_events import NULL
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Reserva(models.Model):
    name = models.CharField(max_length=200, null=False)
    inidate = models.DateTimeField(null=False,default='')
    fimdate = models.DateTimeField(null=False,default='')
    type = models.CharField(max_length=20,null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)


class Estabelecimento(models.Model):
    name = models.CharField(max_length=200, null=False)
    releasedate = models.DateTimeField(null=False)
    type = models.CharField(max_length=20,null=False)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE,null=True)
