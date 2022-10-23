from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Spot

   
def spot(request):
    
    spots = Spot.objects.all()
    context = {'spots': spots}
    return render(request, 'basedailym8/spot.html', context)

def singlespot(request,pk):
    return render(request, 'basedailym8/singlespot.html')

def home(request):
    return render(request, 'main.html')

def reservas(request):
    return render(request, 'reserva.html')

def estacionamento(request):
    return render(request, 'estacionamento.html')

def Praia(request):
    return render(request, 'Praia.html')






