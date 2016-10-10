from django.contrib import admin
from  apps.historiaclinica.models import HistoriaClinica
from apps.paciente.models import Paciente, AntecedenteClinico, AntecedenteFamiliar

# Register your models here.
admin.site.register(HistoriaClinica)
#admin.site.register(Paciente)
#admin.site.register(AntecedenteFamiliar)
#admin.site.register(AntecedenteClinico)
