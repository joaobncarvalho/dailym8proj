from django.urls import path
from . import views


urlpatterns = [
    path('reserva/',views.reserva, name="reserva"),
    path('reserva-single/',views.reservasingle, name="reservasingle"),
    path('estabelecimento/', views.estabelecimento, name="estabelecimento"),
    path('estacionamento/', views.estacionamento, name="estacionamento"),
    path('Praia/', views.Praia, name="Praia"),
    path('', views.home, name="home"),
    
    path('create-reserva/', views.createReserva, name="create-reserva"),
    path('update-reserva/<str:pk>/', views.updateReserva, name="update-reserva"),
    

]
