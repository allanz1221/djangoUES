from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('aula/<int:id>', views.aula, name = 'agenda-events-index'),
    path("aula/guardar", views.guardarCita, name="GuardarCita"),
    path("aula/editar", views.index, name="EditCita"),
    path("aula/borrar", views.index, name="DeleteCita"),
]
