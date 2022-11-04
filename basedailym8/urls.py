from django.urls import path
from . import views


urlpatterns = [
    
    #Paths API Reservas 

    path('mainpage/', views.mainpage, name="mainpage"),
    path('reserva/', views.reserva, name="reserva"),
    path('reserva/<str:pk>/', views.singlereserva, name="singlereserva"),
    path('create-reserva/', views.createReservas, name="create-reserva"),
    path('update-reserva/<str:pk>/', views.updateReservas, name="update-reserva"),
    path('delete-reserva/<str:pk>/', views.deleteReservas, name="delete-reserva"),
    
    #FIM --- Paths API Reservas


    path('register/', views.register, name="register"),
    path('', views.login, name="login"),
    

    path('spot/',views.spot, name="spots"),
    path('spot/<str:pk>/', views.singlespot, name="singlespot"),
    path('estacionamento/', views.estacionamento, name="estacionamento"),
    path('Praia/', views.Praia, name="Praia"),



]
