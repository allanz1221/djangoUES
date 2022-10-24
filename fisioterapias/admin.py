from django.contrib import admin

# Register your models here.
from . models import Cita, Cliente, Aula, Procedencia

class CitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha')
    use_bulk = True

admin.site.register(Cita, CitaAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'procedencia')

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Aula)
admin.site.register(Procedencia)