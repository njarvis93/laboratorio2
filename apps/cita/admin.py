from django.contrib import admin
from apps.centrodesalud.models import Sucursal
from apps.medico.models import Medico
from apps.paciente.models import Paciente

# Register your models here.
admin.site.register(Sucursal)
admin.site.register(Medico)
admin.site.register(Paciente)
