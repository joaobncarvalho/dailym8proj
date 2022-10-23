from django.urls import path
from . import views


urlpatterns = [
    


    path('reserva/',views.reservas, name="reserva"),
    path('', views.spot, name="spots"),
    path('spot/<str:pk>/', views.singlespot, name="singlespot"),
    path('estacionamento/', views.estacionamento, name="estacionamento"),
    path('Praia/', views.Praia, name="Praia"),



]
