from django.contrib import admin
from apps.medico.models import Medico, Especialidad, Horario
from apps.centrodesalud.models import Clinica

# Register your models here.
#admin.site.register(Medico)
admin.site.register(Especialidad)
admin.site.register(Horario)
admin.site.register(Clinica)


