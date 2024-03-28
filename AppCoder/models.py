from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    cod_medico = models.CharField(max_length=10)

    def __str__(self):
        return self.cod_medico

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    cod_paciente = models.CharField(max_length=10)

    def __str__(self):
        return self.cod_paciente

class Farmaco(models.Model):
    nombre = models.CharField(max_length=30)
    matriz_biologica = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model): 
    farmaco = models.ForeignKey(Farmaco, on_delete=models.CASCADE)
    cod_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cod_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()

class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"