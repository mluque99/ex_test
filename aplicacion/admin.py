from django.contrib import admin
from aplicacion.models import Paciente, Medico, Receta

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Receta)
