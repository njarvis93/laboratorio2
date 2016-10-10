from django.db import models

# Create your models here.

class Tratamiento (models.Model):
    duracion = models.TextField()
    tipo = models.CharField(max_length=30)

class Medicamento (models.Model):
    nombre_comun = models.CharField(max_length=20)
    nombre_cientifico = models.CharField(max_length=30)
    principios_activos = models.TextField(max_length=100)
    efectos_secundarios = models.TextField(max_length=100)
    indicaciones = models.TextField(max_length=200)
