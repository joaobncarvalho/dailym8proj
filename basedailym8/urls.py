from django.urls import path
from . import views


urlpatterns = [
    path('reserva/',views.reserva, name="reserva"),
    path('estabelecimento/', views.estabelecimento, name="estabelecimento"),
    path('estacionamento/', views.estacionamento, name="estacionamento"),
    path('PraiaEquipamento/', views.PraiaEquipamento, name="PraiaEquipamento"),
    path('', views.home, name="home"),
    
    

]
