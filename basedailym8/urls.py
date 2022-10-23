from django.urls import path
from . import views


urlpatterns = [
    
    #Paths API Reservas 

    path('reserva/',views.reservas, name="reserva"),
    path('create-reserva/', views.createReservas, name="create-reserva"),
    path('update-reserva/<str:pk>/', views.updateReservas, name="update-reserva"),

    #FIM --- Paths API Reservas 

    path('', views.spot, name="spots"),
    path('spot/<str:pk>/', views.singlespot, name="singlespot"),
    path('estacionamento/', views.estacionamento, name="estacionamento"),
    path('Praia/', views.Praia, name="Praia"),



]
