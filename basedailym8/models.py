from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Pratos(models.Model):
    featured_image =models.ImageField(null=True, blank=True, default="logosemfundo.png")
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=False, default='', blank=False)

    def __str__(self):
        return str(self.name)

class Menu(models.Model):
    
    featured_image =models.ImageField(null=True, blank=True, default="logosemfundo.png")
    name = models.CharField(max_length=200, null=False)
    pratos = models.ManyToManyField(Pratos)

    def __str__(self):
        return str(self.name)

class Restaurante(models.Model):
    RESTAURANTE_TYPE = (
        ('Internacional','rest_internacional'),
        ('Americano','rest_americano'),
        ('Português','rest_portugues'),
        ('Chinês','rest_chines'),
        ('Italiano','rest_italiano'),
        ('Japonês','rest_japones'),
    )
    featured_image =models.ImageField(null=True, blank=True, default="logosemfundo.png")
    name = models.CharField(max_length=200, null=False)
    releasedate = models.DateTimeField(null=False)
    type = models.CharField(max_length=20,choices=RESTAURANTE_TYPE,null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,null=True,blank=True)
    Menu_image =models.ImageField(null=True, blank=True, default="logo.png")
    

    def __str__(self):
        return str(self.name)



class Estacionamento(models.Model):
    featured_image =models.ImageField(null=True, blank=True, default="logosemfundo.png")
    name = models.CharField(max_length=200, null=False)
    releasedate = models.DateTimeField(null=False)
    lugares = models.IntegerField(null=False, blank = False, default='')
    
    

    def __str__(self):
        return str(self.name)


class Spot(models.Model):
    
    
    featured_image =models.ImageField(null=True, blank=True, default="logosemfundo.png")
    name = models.CharField(max_length=200, null=False)
    releasedate = models.DateTimeField(null=False)
 

    def __str__(self):
        return str(self.name)

class Reserva(models.Model):
    RESERVA_TYPE =(('Almoço', 'almoco'), 
    ('Lanche', 'lanche'), 
    ('Jantar', 'jantar'), 
    ('Beber um Copo', 'copo'))
    name = models.ForeignKey(Spot, on_delete=models.CASCADE,null=True,blank=True)
    inidate = models.DateTimeField(null=False)
    fimdate = models.DateTimeField(null=False)
    type = models.CharField(max_length=20,choices=RESERVA_TYPE,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.name)

class Praia(models.Model):
    name = models.CharField(max_length=100, null=False)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE,null=True, blank=True)

        
    def __str__(self):
        return self.name

class Praiaequip(models.Model):
    
    EQUIPAMENTO_TYPE = (
        ('Espreguiçadeira','equi_espreguicadeira'),
        ('Toldo','equi_toldo'),
    )
    
    featured_image =models.ImageField(null=True, blank=True, default="logosemfundo.png")
    releasedate = models.DateTimeField(null=False)
    equipamentos = models.IntegerField(null=False, blank = False, default='')
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE,null=True,blank=True)
    type = models.CharField(max_length=20,choices=EQUIPAMENTO_TYPE,null=False)
    praia = models.ForeignKey(Praia, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.praia)


