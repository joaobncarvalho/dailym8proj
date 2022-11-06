from django.urls import path
from . import views


urlpatterns = [
    
    #Paths API Reservas 

   
    path('reserva/', views.reserva, name="reserva"),
    path('reserva/<str:pk>/', views.singlereserva, name="singlereserva"),
    path('create-reserva/', views.createReservas, name="create-reserva"),
    path('update-reserva/<str:pk>/', views.updateReservas, name="update-reserva"),
    path('delete-reserva/<str:pk>/', views.deleteReservas, name="delete-reserva"),
    
    #FIM --- Paths API Reservas

    path('', views.mainpage, name="mainpage"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    
    #RESTAURANTES

    path('restaurant/',views.restaurants, name="restaurants"),
    path('restaurant/<str:pk>/', views.restaurantsingle, name="restaurantsingle"),
    
    #FIM -- RESTAURANTES
    
    #ESTACIONAMENTOS

    path('parking/',views.parking, name="parkings"),
    path('parking/<str:pk>/', views.restaurantsingle, name="restaurantsingle"),
    
    #FIM -- ESTACIONAMENTOS


     #EQUIPAMENTOS

    path('equip/',views.equips, name="equips"),
    path('equip/<str:pk>/', views.equipsingle, name="equip"),
    
    #FIM -- EQUIPAMENTOS



    
    path('spot/',views.spot, name="spots"),
    path('spot/<str:pk>/', views.singlespot, name="singlespot"),
    path('estacionamento/', views.estacionamento, name="estacionamento"),
    path('Praia/', views.Praia, name="Praia"),



]
