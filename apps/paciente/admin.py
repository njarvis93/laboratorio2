from django.contrib import admin
from  apps.tratamiento.models import Tratamiento
from  apps.medico.models import Medico
from  apps.paciente.models import Paciente, AntecedenteClinico, AntecedenteFamiliar

# Register your models here.
#admin.site.register(Medico)
admin.site.register(Tratamiento)
#admin.site.register(Paciente)
admin.site.register(AntecedenteFamiliar)
admin.site.register(AntecedenteClinico)
