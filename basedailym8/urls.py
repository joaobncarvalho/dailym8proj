from django.urls import path
from . import views, include 


urlpatterns = [
    path('', views.home, name="home"),
    path('room/',views.room, name="room"),
]
