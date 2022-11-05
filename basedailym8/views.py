from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Spot
from .models import Reserva
from .forms import ReservaForm
from .models import Restaurante




def register(request):
    return render(request, 'homeregister.html')

def login(request):
    return render(request, 'homelogin.html')

def mainpage(request):
    return render(request, 'mainpage.html')




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

# RESERVAS

def reserva(request):
    reservas = Reserva.objects.all()
    context = {'reservas':reservas}
    return render(request, 'basedailym8/reserva.html', context)

def singlereserva(request,pk):
    reserva = Reserva.objects.get(id=pk)
    context = {'reserva': reserva}
    return render(request, 'basedailym8/reservasingle.html', context)

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


def deleteReservas(request,pk):
    reserva = Reserva.objects.get(id=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('/')
    
    context = {'object': reserva}
    return render(request, 'basedailym8/delete_template.html', context)

#FIM --- RESERVAS

#RESTAURANTS


def restaurants(request):
    
    restaurants = Restaurante.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'basedailym8/restaurants.html', context)

def restaurantsingle(request,pk):
    
    restaurant = Restaurante.objects.get(id=pk)
    context = {'restaurant': restaurant}
    return render(request, 'basedailym8/restaurantsingle.html', context)

def estacionamento(request):
    return render(request, 'estacionamento.html')

def Praia(request):
    return render(request, 'Praia.html')






