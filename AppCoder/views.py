from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Medico, Solicitud, Paciente, Farmaco
from AppCoder.forms import FormularioMedico, FormularioPaciente, FormularioSolicitud, FormularioFarmaco, AvatarForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test




# Create your views here.

def inicio(request):
    return render(request, "inicio.html")  

def sobre_mi(request):
    return render(request, "sobre_mi.html")  

#Permisos de administrador

def es_administrador(user):
    return user.is_authenticated and user.is_superuser

def no_permiso(request):
    return render(request, 'no_permiso.html')

####### CRUD de Médico #######

@login_required
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

            messages.success(request, "El médico ha sido creado con éxito.")

            return redirect("Inicio")
    
    else:
            
        formulario_medico1 = FormularioMedico()

    return render(request, "crear_medicos.html", {"form1":formulario_medico1})

def ver_medicos(request):

    todos_medicos = Medico.objects.all()

    return render(request, "ver_medicos.html", {"total":todos_medicos})

@login_required
def actualizar_medico(request, id_medico):
    medico_seleccionado = Medico.objects.get(id=id_medico)

    if request.method == "POST":
        formulario_medico = FormularioMedico(request.POST, instance=medico_seleccionado)
        if formulario_medico.is_valid():
            formulario_medico.save()
            return render(request, "inicio.html")
    else:
        formulario_medico = FormularioMedico(instance=medico_seleccionado)

    return render(request, "actualizar_medicos.html", {"form1": formulario_medico})

@login_required
def borrar_medico(request, id_medico):
        
    medico_seleccionado = Medico.objects.get(id = id_medico)

    medico_seleccionado.delete()

    return render(request, "inicio.html") 

####### CRUD de Farmaco #######

@login_required
@user_passes_test(es_administrador, login_url='no permiso')

def crear_farmaco(request):

    if request.method == "POST":

        formulario_farmaco1 = FormularioFarmaco(request.POST)

        if formulario_farmaco1.is_valid():
            
            info = formulario_farmaco1.cleaned_data

            farmaco = Farmaco(nombre=info["nombre"], 
                                matriz_biologica=info["matriz_biologica"])

            farmaco.save()

            messages.success(request, "El nuevo fármaco ha sido creado con éxito.")

            return redirect("Inicio")
    
    else:
            
        formulario_farmaco1 = FormularioFarmaco()

    return render(request, "crear_farmaco.html", {"form1":formulario_farmaco1})

def ver_farmaco(request):

    todos_farmacos = Farmaco.objects.all()

    return render(request, "ver_farmaco.html", {"total":todos_farmacos})

@login_required
@user_passes_test(es_administrador, login_url='/no permiso/')
def actualizar_farmaco(request, id_farmaco):

    farmaco_seleccionado = Farmaco.objects.get(id=id_farmaco)

    if request.method == "POST":

        formulario_farmaco1 = FormularioFarmaco(request.POST, instance=farmaco_seleccionado)

        if formulario_farmaco1.is_valid():

            formulario_farmaco1.save()

            return render(request, "crear_farmaco.html")
    else:
        formulario_farmaco1 = FormularioPaciente(instance=farmaco_seleccionado)

    return render(request, "actualizar_farmaco.html", {"form1": farmaco_seleccionado})

@login_required
@user_passes_test(es_administrador, login_url='/no permiso/')
def borrar_farmaco(request, id_farmaco):
        
    farmaco_seleccionado = Farmaco.objects.get(id = id_farmaco)

    farmaco_seleccionado.delete()

    return render(request, "inicio.html")


####### CRUD de PACIENTE #######

@login_required
def crear_paciente(request):

    if request.method == "POST":

        formulario_paciente1 = FormularioPaciente(request.POST)

        if formulario_paciente1.is_valid():
            
            info = formulario_paciente1.cleaned_data

            paciente = Paciente(nombre=info["nombre"], 
                                apellido=info["apellido"], 
                                edad=info["edad"], 
                                cod_paciente=info["cod_paciente"])

            paciente.save()

            messages.success(request, "El paciente ha sido creado con éxito.")

            return redirect("Inicio")
    
    else:
            
        formulario_paciente1 = FormularioPaciente()

    return render(request, "crear_pacientes.html", {"form1":formulario_paciente1})

def ver_pacientes(request):

    todos_pacientes = Paciente.objects.all()

    return render(request, "ver_pacientes.html", {"total":todos_pacientes})

@login_required
def actualizar_paciente(request, id_paciente):
    paciente_seleccionado = Paciente.objects.get(id=id_paciente)
   
    if request.method == "POST":
        formulario_paciente = FormularioPaciente(request.POST, instance=paciente_seleccionado)
        if formulario_paciente.is_valid():
            formulario_paciente.save()
            return render(request, "inicio.html")
        
    else:
        formulario_paciente = FormularioPaciente(instance=paciente_seleccionado)

    return render(request, "actualizar_pacientes.html", {"form1": formulario_paciente})

@login_required
def borrar_pacientes(request, id_paciente):
        
    paciente_seleccionado = Paciente.objects.get(id = id_paciente)

    paciente_seleccionado.delete()

    return render(request, "inicio.html")



####### CRUD de Solicitud #######

@login_required
def crear_solicitud(request):

    if request.method == "POST":
        formulario_solicitud = FormularioSolicitud(request.POST)

        if formulario_solicitud.is_valid():
            info = formulario_solicitud.cleaned_data
            nueva_solicitud = Solicitud(
                farmaco=info["farmaco"],
                cod_paciente=info["cod_paciente"],
                cod_medico=info["cod_medico"],
                fecha=info["fecha"]
            )
            nueva_solicitud.save()

            messages.success(request, "La solicitud ha sido completada con éxito.")
            return render(request, "inicio.html")

    else:
        formulario_solicitud = FormularioSolicitud()

    return render(request, "crear_solicitudes.html", {"form1": formulario_solicitud})

@login_required
def ver_solicitudes(request):
    todas_solicitudes = Solicitud.objects.all()
    return render(request, "ver_solicitudes.html", {"total": todas_solicitudes})

@login_required
def actualizar_solicitud(request, id_solicitud):
    solicitud_seleccionada = Solicitud.objects.get(id=id_solicitud)
   
    if request.method == "POST":
        formulario_solicitud = FormularioSolicitud(request.POST, instance=solicitud_seleccionada)
        if formulario_solicitud.is_valid():
            formulario_solicitud.save()
            return render(request, "inicio.html")
        
    else:
        formulario_solicitud = FormularioSolicitud(instance=solicitud_seleccionada)

    return render(request, "actualizar_solicitudes.html", {"form1": formulario_solicitud})

@login_required
def borrar_solicitud(request, id_solicitud):
    solicitud_seleccionada = Solicitud.objects.get(id=id_solicitud)
    solicitud_seleccionada.delete()
    return render(request, "inicio.html")
  


####### BUSCAR SOLICITUDES #######

@login_required
def buscar_solicitudes(request):

    filtrar_solicitud = None  # Inicializa la variable fuera del bloque 'if'

    if 'cod_paciente' in request.GET:

        cod_paciente = request.GET['cod_paciente']
        filtrar_solicitud = Solicitud.objects.filter(cod_paciente__cod_paciente__icontains=cod_paciente)
        mensaje = f"Se ha buscado la solicitud para el paciente {request.GET['cod_paciente']}"
    
    else:

        mensaje = "Para buscar una solicitud debes ingresar los datos de búsqueda."

    return render(request, "buscar_solicitudes.html", {"mensaje": mensaje, "resultados": filtrar_solicitud})


# Iniciar sesion

def iniciar_sesion(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario = authenticate(username=info["username"], password = info["password"])

            if usuario is not None:

                login(request, usuario)

                return render(request, "inicio.html")
            
        else:

            return render(request, "inicio.html", {"aviso": "Nombre de usuario o contraseña ingresados son incorrectos."})
    
    else:

        formulario = AuthenticationForm()

    return render(request, "inicio_sesion.html", {"form1":formulario})
    

# Registrarse

def registrarse(request):
    if request.method == "POST":
        formulario_usuario = UserCreationForm(request.POST)
        formulario_avatar = AvatarForm(request.POST, request.FILES) 

        if formulario_usuario.is_valid() and formulario_avatar.is_valid():
            usuario = formulario_usuario.save()
            avatar = formulario_avatar.save(commit=False)
            avatar.user = usuario 
            avatar.save()
            return redirect("Inicio") 
    else:
        formulario_usuario = UserCreationForm()
        formulario_avatar = AvatarForm()

    return render(request, "registro.html", {"form_usuario": formulario_usuario, "form_avatar": formulario_avatar})

# Cerrar sesion

def cerrar_sesion(request):

    logout(request)

    return render(request, "inicio.html", {"mensaje":"Se ha cerrado su sesión de forma exitosa."})

    






