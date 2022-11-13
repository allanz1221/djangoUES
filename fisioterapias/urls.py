from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('aula/<int:id>', views.aula, name = 'agenda'),
    path("aula/guardar", views.guardarCita, name="GuardarCita"),
    path("paciente/guardar", views.guardarPaciente, name="GuardarPaciente"),
    path("citas", views.citas, name="Citas"),
    path("reportes", views.reportes, name="Reportes"),
]
