from django.contrib import admin

# Register your models here.


from .models import Reserva
from .models import Spot
from .models import Estacionamento
from .models import Praia

admin.site.register(Reserva)
admin.site.register(Spot)
admin.site.register(Estacionamento)
admin.site.register(Praia)


