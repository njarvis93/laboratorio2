from django.db import models
from apps.centrodesalud.models import Clinica

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=20)
    area = models.CharField(max_length=20)

class Medico(models.Model):
    nro_registro = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    direccion = models.TextField(max_length=50)
    fecha_nacimiento = models.DateField()
    especialidad = models.ManyToManyField(Especialidad)
    clinica = models.ManyToManyField(Clinica)
    descripcion = models.TextField(max_length=300)
    estudios = models.TextField(max_length=100);
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/')

class Horario(models.Model):
    fecha = models.DateField()
    hora_inicio = models.DateTimeField(auto_now=False, auto_now_add=False)
    hora_fin = models.DateTimeField(auto_now=False, auto_now_add=False)
    doctor = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)

    
        