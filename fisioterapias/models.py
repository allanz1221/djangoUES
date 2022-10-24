from django.db import models

# Create your models here.

class Procedencia(models.Model):
    procedencia = models.CharField(max_length=200)

    def __str__(self):
        return self.procedencia

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    procedencia = models.ForeignKey(Procedencia, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Aula(models.Model):
    aula = models.CharField(max_length=200)
    
    def __str__(self):
        return self.aula

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    cumplio = models.BooleanField()
    costo = models.FloatField()

    def __str__(self):
        return self.cliente.nombre
