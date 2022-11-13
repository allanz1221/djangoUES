from django.db import models
from django.contrib.auth.models import User

class ProgramaEducativo(models.Model):
    nombre = models.CharField(max_length=200, blank=False)
    siglas = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.nombre

class Procedencia(models.Model):
    procedencia = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.procedencia

class Paciente(models.Model):
    nombre = models.CharField(max_length=200, blank=False)
    procedencia = models.ForeignKey(Procedencia, on_delete=models.CASCADE, blank=True)
    expediente = models.CharField(max_length=200, blank=True)
    programaeducativo = models.ForeignKey(ProgramaEducativo, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nombre

class Aula(models.Model):
    nombre = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, blank=False)
    motivo = models.CharField(max_length=200, blank=False)
    fecha = models.DateField(blank=False)
    hora_inicio = models.TimeField(blank=False)
    hora_cierre = models.TimeField(blank=False)
    cumplio = models.BooleanField(default='0')
    costo = models.FloatField(blank=True)
    comentarios = models.CharField(max_length=240, blank=True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.paciente.nombre

class CierreCaja(models.Model):
    fecha = models.DateTimeField(blank=False)
    cantidad = models.FloatField(blank=False)
    comentarios = models.CharField(max_length=200, blank=True)

    def __str__(self):
        fecha_nueva = str(self.fecha)
        return fecha_nueva