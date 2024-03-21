from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Medico, Solicitud, Paciente
from AppCoder.forms import FormularioMedico

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")   

def ver_medicos(request):
    return render(request, "ver_medicos.html")   

def ver_pacientes(request):
    return render(request, "ver_pacientes.html")   

def ver_solicitudes(request):
    return render(request, "ver_solicitudes.html")    


##CRUD de Solicitud

def crear_solicitud(request):

    if request.method == 'POST':

        nueva_solicitud = Solicitud(num_paciente=request.POST["num_paciente"], num_medico=request.POST["num_medico"])
        nueva_solicitud.save()
        
    else:

        pass

    return render(request, "crear_solicitudes.html")


##CRUD de Paciente

def crear_paciente(request):

    if request.method == 'POST':

        pass

    else:
        
        pass

    return render(request, "crear_pacientes.html")


##CRUD de Médico

def crear_medico(request):

    if request.method == "POST":

        formulario_medico1 = FormularioMedico(request.POST)

        if formulario_medico1.is_valid():
            
            info = formulario_medico1.cleaned_data

            medico = Medico(nombre=info["nombre"], 
                             apellido=info["apellido"], 
                             email=info["email"], 
                             cod_medico=info["cod_medico"])

            medico.save()

            return render(request, "inicio.html")
    
    else:
            
        formulario_medico1 = FormularioMedico()

    return render(request, "crear_medicos.html", {"form1":formulario_medico1})

    #def registro_medico(request):
    #if request.method == "POST":
        #medico = Medico(cod_medico=request.POST["cod_medico"])
#nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"], 
        #medico.save()
        #return render(request, "AppCoder/inicio.html")


## Busqueda de solicitudes 

def buscar_solicitudes(request):

    if request.GET["cod_paciente"]:

        cod_paciente = request.GET["cod_paciente"]
        filtrar_solicitud = Solicitud.objects.filter(cod_paciente__icontains=cod_paciente)

        mensaje = f"Se ha buscado la solicitud para el paciente {request.GET["cod_paciente"]}"
    
    else:

        mensaje = "Para buscar una solicitud debes ingresar los datos de busqueda"

    return render(request, "buscar_solicitudes.html", {"mensaje":mensaje, "resultados":filtrar_solicitud})

