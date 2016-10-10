from django.db import models
from  apps.tratamiento.models import Tratamiento
from  apps.medico.models import Medico
# Create your models here.

class Paciente(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    peso = models.IntegerField()
    estatura = models.IntegerField()


class AntecedenteFamiliar (models.Model):
    descripcion = models.TextField(max_length=100)
    fecha_aproximada = models.DateField()
    parentesco = models.CharField(max_length=20)
    tratamiento = models.ForeignKey(Tratamiento, null=True, blank=True, on_delete=models.CASCADE)


class AntecedenteClinico (models.Model):
    descripcion = models.TextField(max_length=100)
    fecha_registro = models.DateField()
    tratamiento = models.ForeignKey(Tratamiento, null=True, blank=True, on_delete=models.CASCADE)
    medico_tratante = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)


