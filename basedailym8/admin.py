from django.contrib import admin

# Register your models here.


from .models import Reserva
from .models import Estabelecimento

admin.site.register(Reserva)
admin.site.register(Estabelecimento)

