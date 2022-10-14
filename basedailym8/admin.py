from django.contrib import admin

# Register your models here.


from .models import Reserva
from .models import Estabelecimento
from .models import Estacionamento
from .models import PraiaEquipamento

admin.site.register(Reserva)
admin.site.register(Estabelecimento)
admin.site.register(Estacionamento)
admin.site.register(PraiaEquipamento)


