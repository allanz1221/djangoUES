from django.contrib import admin

# Register your models here.
from . models import Cita, Cliente, Aula, Procedencia, CierreCaja

admin.site.site_header = "Sitio web de Registro de Fisiterapias"
admin.site.site_title = "Universidad Estatal de Sonora"
admin.site.index_title = "Bienvenidos al portal de administración"


class CitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha')
    use_bulk = True

admin.site.register(Cita, CitaAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'procedencia')

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Aula)
admin.site.register(Procedencia)

class Cierre(admin.ModelAdmin):
    list_display = ('cajero', 'fecha', 'cantidad')
    use_bulk = True

admin.site.register(CierreCaja, Cierre)