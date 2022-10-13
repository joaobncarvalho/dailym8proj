from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reserva(models.Model):
    name = models.CharField(max_length=200, null=False)
    date = models.DateTimeField(null=False)
    type = models.CharField(max_length=20,null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

