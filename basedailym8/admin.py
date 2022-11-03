from django.contrib import admin

# Register your models here.


from .models import Reserva
from .models import Spot
from .models import Estacionamento
from .models import Praia
from .models import Pratos
from .models import Menu
from .models import Restaurante
from .models import Praiaequip




admin.site.register(Reserva)
admin.site.register(Spot)
admin.site.register(Restaurante)
admin.site.register(Estacionamento)
admin.site.register(Praia)
admin.site.register(Pratos)
admin.site.register(Menu)
admin.site.register(Praiaequip)


