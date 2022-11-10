from django.db import models


# Create your models here.

class PE(models.Model):
    programa_educativo = models.CharField(max_length=200, blank=False)
    siglas = models.CharField(max_length=200, blank=False)

class Procedencia(models.Model):
    procedencia = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.procedencia

class Cliente(models.Model):
    nombre = models.CharField(max_length=200, blank=False)
    procedencia = models.ForeignKey(Procedencia, on_delete=models.CASCADE, blank=False)
    expediente = models.CharField(max_length=200, blank=False)
    PE = models.ForeignKey(PE, on_delete=models.CASCADE, blank=True)

class Aula(models.Model):
    aula = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.aula

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, blank=False)
    motivo = models.CharField(max_length=200, blank=False)
    fecha = models.DateTimeField(blank=False)
    hora_cierre = models.TimeField(blank=False)
    cumplio = models.BooleanField(default='0')
    costo = models.FloatField(blank=True)

    def __str__(self):
        return self.cliente.nombre

class CierreCaja(models.Model):
    cajero = models.CharField(max_length=200)
    fecha = models.DateTimeField(blank=False)
    cantidad = models.FloatField(blank=False)
    comentarios = models.CharField(max_length=200, blank=True)    