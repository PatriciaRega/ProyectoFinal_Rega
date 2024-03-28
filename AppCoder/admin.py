from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Medico)

admin.site.register(Paciente)

admin.site.register(Solicitud)

admin.site.register(Farmaco)

admin.site.register(Avatar)