from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="agenda-events-index"),
    path("", views.index, name="GuardarCita"),
    path("", views.index, name="EditCita"),
    path("", views.index, name="DeleteCita"),
]
