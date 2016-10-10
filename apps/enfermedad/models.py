from django.db import models

# Create your models here.
class Enfermedad (models.Model):
    nombre = models.CharField(max_length=20)
    nombre_cientifico = models.CharField(max_length=20)
    epidemiologia = models.CharField(max_length=30)
    duracion = models.CharField(max_length=10)
    distribucion = models.CharField(max_length=20)

class CuadroClinico (models.Model):
    descripcion = models.TextField(max_length=50)
    nombre_formal = models.CharField(max_length=20)
    nombre_comun = models.CharField(max_length=20)