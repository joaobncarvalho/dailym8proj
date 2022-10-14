from django.urls import path
from . import views


urlpatterns = [
    path('reserva/',views.reserva, name="reserva"),
    path('estabelecimento/', views.estabelecimento, name="estabelecimento"),
    path('', views.home, name="home"),
    
    

]
