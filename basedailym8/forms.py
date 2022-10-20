from dataclasses import fields
from django.forms import ModelForm
from .models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['name','inidate','fimdate','type']