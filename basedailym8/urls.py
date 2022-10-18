from django.urls import path
from . import views


urlpatterns = [
    path('reserva/',views.reserva, name="reserva"),
    path('estabelecimento/', views.estabelecimento, name="estabelecimento"),
    path('estacionamento/', views.estacionamento, name="estacionamento"),
    path('Praia/', views.Praia, name="Praia"),
    path('', views.home, name="home"),
    
    

]
