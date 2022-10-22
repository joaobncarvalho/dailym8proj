from multiprocessing import context
from django.shortcuts import render, redirect







def home(request):
    return render(request, 'main.html')

def reservas(request):
    return render(request, 'reserva.html')
   
    
def spot(request):
    return render(request, 'spot.html')

def singlespot(request,pk):
    return render(request, 'singlespot.html')

def estacionamento(request):
    return render(request, 'estacionamento.html')

def Praia(request):
    return render(request, 'Praia.html')






