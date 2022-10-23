from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Spot
from .models import Reserva
from .forms import ReservaForm



#SPOTS

def spot(request):
    
    spots = Spot.objects.all()
    context = {'spots': spots}
    return render(request, 'basedailym8/spot.html', context)

def singlespot(request,pk):
    return render(request, 'basedailym8/singlespot.html')

#FIM --- SPOTS

def home(request):
    return render(request, 'main.html')

#CRUD for reservas 

def reservas(request):
    return render(request, 'reserva.html')

def createReservas(request):
    form = ReservaForm()

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva')

    context = {'form':form}
    return render(request, "basedailym8/reserva_form.html", context)

def updateReservas(request,pk):
    
    reserva = Reserva.objects.get(id=pk)
    form = ReservaForm(instance=reserva)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva')

    context = {'form':form}
    return render(request, "basedailym8/reserva_form.html", context)

#FIM --- CRUD for reservas 

def estacionamento(request):
    return render(request, 'estacionamento.html')

def Praia(request):
    return render(request, 'Praia.html')






