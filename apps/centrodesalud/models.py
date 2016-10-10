from django.db import models

# Create your models here.

class Clinica (models.Model):
    nombre = models.CharField(max_length=50)
    tipo= models.IntegerField() #1=Public 0=Private

class Sucursal (models.Model):
    direccion = models.TextField(max_length=50)
    telefono = models.CharField(max_length=12)
    director = models.CharField(max_length=20, blank=True)
    clinica = models.ForeignKey(Clinica, null=False, blank=False, on_delete=models.CASCADE)

