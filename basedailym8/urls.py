from django.urls import path
from . import views


urlpatterns = [
    


    path('reserva/',views.reservas, name="reserva"),
    path('spot/', views.spot, name="spot"),
    path('singlespot/<str:pk>/', views.singlespot, name="singlespot"),
    path('estacionamento/', views.estacionamento, name="estacionamento"),
    path('Praia/', views.Praia, name="Praia"),
    path('', views.home, name="home"),



]
