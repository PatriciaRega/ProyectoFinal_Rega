from django.urls import path
from AppCoder.views import *

urlpatterns = [
    
    path("", inicio, name="Inicio"),

    path("login/", iniciar_sesion, name="Iniciar sesion"),
    path("signup/", registrarse, name="Crear usuario"),
    path("logout/", cerrar_sesion, name="Cerrar sesion"),

    #URLS CRUD DEL MODELO

    path("crear_medicos/", crear_medico, name = 'crear medicos'),
    path("ver_medicos/", ver_medicos, name = 'ver medicos'),
    path("actualizar_medicos/<id_medico>", actualizar_medico, name = "Editar"),
    path("borrar_medicos/<id_medico>", borrar_medico, name = "Eliminar"),

    path("crear_pacientes/", crear_paciente, name = 'crear pacientes'),
    path("ver_pacientes/", ver_pacientes, name = 'ver pacientes'),

    path("crear_solicitudes/", crear_solicitud, name = 'crear solicitudes'),
    path("ver_solicitudes/", ver_solicitudes, name = 'ver solicitudes'),
    
    #URLS DE BUSQUEDA

    path("buscar_solicitudes/", buscar_solicitudes, name = 'buscar solicitudes')
  
    ]
