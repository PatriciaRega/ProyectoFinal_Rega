from django.db import models

# Create your models here.

class Medico(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    cod_medico = models.CharField(max_length=30)

class Solicitud(models.Model):
    farmaco = models.CharField(max_length=60)
    cod_paciente = models.CharField(max_length=30)
    cod_medico = models.CharField(max_length=30)
    fecha = models.DateField()

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    cod_paciente = models.CharField(max_length=30)
