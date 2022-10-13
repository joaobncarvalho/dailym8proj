from django.urls import path
from . import views


urlpatterns = [
    path('reserva/',views.reserva, name="reserva"),
    path('', views.home, name="home"),
    
    

]
