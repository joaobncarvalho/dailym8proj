from django.shortcuts import render



reserva = [
{'id':1, 'name':'DailyM8 Project'},
{'id':2, 'name':'DailyM8 Developers'},
{'id':3, 'name':'DailyM8 Users'}

]

def home(request):
    context = {'reserva': reserva}
    context = {'estabelecimento': estabelecimento}
    context = {'Praia': Praia}
    return render(request, 'home.html', context)

def reserva(request):
    return render(request, 'reservas.html')


def estabelecimento(request):
    return render(request, 'estabelecimento.html')

def estacionamento(request):
    return render(request, 'estacionamento.html')

def Praia(request):
    return render(request, 'Praia.html')





