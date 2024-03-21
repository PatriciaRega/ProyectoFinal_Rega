from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("crear_medicos/", crear_medico, name = 'crear medicos'),
    path("crear_pacientes/", crear_paciente, name = 'crear pacientes'),
    path("crear_solicitudes/", crear_solicitud, name = 'crear solicitudes'),
    path("ver_medicos/", ver_medicos, name = 'ver medicos'),
    path("ver_pacientes/", ver_pacientes, name = 'ver pacientes'),
    path("buscar_solicitudes/", buscar_solicitudes, name = 'buscar solicitudes'),
    path("", inicio, name="Home")
    ]
