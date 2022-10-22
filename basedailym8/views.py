from multiprocessing import context
from django.shortcuts import render, redirect


   
def spot(request):
    return render(request, 'basedailym8/spot.html')

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






