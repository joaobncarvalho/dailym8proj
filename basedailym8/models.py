from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Spot(models.Model):
    SPOT_TYPE = (
        ('Restaurante','spot_restaurante'),
        ('Bar','spot_bar'),
        ('Cafe','spot_cafe'),
        ('Discoteca','spot_disco'),
        ('Bar de Praia','spot_bardepraia'),
    )
    name = models.CharField(max_length=200, null=False)
    releasedate = models.DateTimeField(null=False)
    type = models.CharField(max_length=20,choices=SPOT_TYPE,null=False)
    

    def __str__(self):
        return str(self.name)


class Reserva(models.Model):
    RESERVA_TYPE = (
        ('Almoço','almoco'),
        ('Lanche','lanche'),
        ('Jantar','jantar'),
        ('Beber um Copo','copo'),
    )
    name = models.ForeignKey(Spot, on_delete=models.CASCADE,null=True,blank=True)
    inidate = models.DateTimeField(null=False,default='')
    fimdate = models.DateTimeField(null=False,default='')
    type = models.CharField(max_length=20,choices=RESERVA_TYPE,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.name)

class Estacionamento(models.Model):
    name = models.CharField(max_length=200, null=False)
    lugares = models.IntegerField(null=True)
    EstEstabelecimento = models.ForeignKey(Spot, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class Praia(models.Model):
    name = models.CharField(max_length=100, null=False)
    NumeroEquipamentos = models.IntegerField(default='',null=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name