from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Medico, Solicitud, Paciente

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")   

def ver_medicos(request):
    return render(request, "ver_medicos.html")   

def ver_pacientes(request):
    return render(request, "ver_pacientes.html")   

def ver_solicitudes(request):
    return render(request, "ver_solicitudes.html")    



def crear_solicitud(request):

    if request.method == 'POST':

        nueva_solicitud = Solicitud(num_paciente=request.POST["num_paciente"], num_medico=request.POST["num_medico"])
        nueva_solicitud.save()
        
    else:

        pass

    return render(request, "crear_solicitudes.html")

def crear_paciente(request):

    if request.method == 'POST':

        pass

    else:
        
        pass

    return render(request, "crear_pacientes.html")

def crear_medico(request):

    if request.method == 'POST':

        pass

    else:
        
        pass

    return render(request, "crear_medicos.html")

