from django.db import models


# Create your models here.

class Medico(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    cod_medico = models.CharField(max_length=10)

class Solicitud(models.Model):  #idea: cambiar como se hace la solicitud y que se muestre como fecha, farmaco, nombre paciente, codigo paciente, codigo medico
    farmaco = models.CharField(max_length=60)
    cod_paciente = models.CharField(max_length=30)
    cod_medico = models.CharField(max_length=10)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.fecha} - {self.farmaco} - {self.cod_paciente} - {self.cod_medico}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    cod_paciente = models.CharField(max_length=10)
