from django.db import models
from apps.paciente.models import Paciente, AntecedenteClinico, AntecedenteFamiliar

# Create your models here.
class HistoriaClinica (models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    ante_familiares = models.ForeignKey(AntecedenteFamiliar, null=False, blank=False, on_delete=models.CASCADE)
    ante_clinicos = models.ForeignKey(AntecedenteClinico, null=True, blank=False, on_delete=models.CASCADE)
