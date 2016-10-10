from django.db import models
from apps.centrodesalud.models import Sucursal
from apps.medico.models import Medico
from apps.paciente.models import Paciente


# Create your models here.
class Cita (models.Model):
    medico = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion_sintomas = models.TextField(null=True, blank=True)
    tipo = models.IntegerField() # 1. Consulta 2. Entrega de Resultados
