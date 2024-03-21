from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Medico, Solicitud, Paciente
from AppCoder.forms import FormularioMedico

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")   


##CRUD de Solicitud

def crear_solicitud(request):

    if request.method == 'POST':

        nueva_solicitud = Solicitud(farmaco=request.POST["farmaco"], cod_paciente=request.POST["cod_paciente"], cod_medico=request.POST["cod_medico"], fecha=request.POST["fecha"])
        nueva_solicitud.save()
        
    else:

        pass

    return render(request, "crear_solicitudes.html")

def ver_solicitudes(request):

    todas_solucitudes = Solicitud.objects.all()

    return render(request, "ver_solicitudes.html", {"total":todas_solucitudes})    

##CRUD de Paciente

def ver_pacientes(request):
    return render(request, "ver_pacientes.html")   

def crear_paciente(request):

    if request.method == 'POST':

        pass

    else:
        
        pass

    return render(request, "crear_pacientes.html")

def ver_pacientes(request):

    todos_pacientes = Solicitud.objects.all()

    return render(request, "ver_solicitudes.html", {"total":todos_pacientes})  

#def acutalizar_paciente(request, id_paciente):

   # paciente_elegido = Paciente.objects.get(nombre=id_paciente)




##CRUD de Médico

def ver_medicos(request):
    return render(request, "ver_medicos.html")   

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

def ver_medico(request):

    todos_medicos = Medico.objects.all()

    return render(request, "ver_medicos.html", {"total":todos_medicos})

def actualizar_medico(request, id_medico):
        
    medico_seleccionado = FormularioMedico.objects.get(id = id_medico)

    if medico_seleccionado.is_valid():
            
            info = formulario_medico1.cleaned_data

            medico_seleccionado.nombre = info["nombre"], 
            medico_seleccionado.apellido=info["apellido"], 
            medico_seleccionado.email=info["email"], 
            medico_seleccionado.cod_medico=info["cod_medico"]

            medico_seleccionado.save()

            return render(request, "inicio.html")
    
    else:
            
        formulario_medico1 = FormularioMedico(initial={"nombre":medico_seleccionado.nombre,
                                                       "apellido":medico_seleccionado.apellido,
                                                       "email":medico_seleccionado.email,
                                                       "cod_medico":medico_seleccionado
                                                       })

    return render(request, "actualizar_medicos.html", {"form1":formulario_medico1})

def borrar_medico(request, id_medico):
        
    medico_seleccionado = Medico.objects.get(id = id_medico)

    medico_seleccionado.delete()

    return render(request, "inicio.html") 
   

def buscar_solicitudes(request):

    if request.GET["cod_paciente"]:

        cod_paciente = request.GET["cod_paciente"]
        filtrar_solicitud = Solicitud.objects.filter(cod_paciente__icontains=cod_paciente)

        mensaje = f"Se ha buscado la solicitud para el paciente {request.GET["cod_paciente"]}"
    
    else:

        mensaje = "Para buscar una solicitud debes ingresar los datos de busqueda"

    return render(request, "buscar_solicitudes.html", {"mensaje":mensaje, "resultados":filtrar_solicitud})

