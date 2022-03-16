from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesión = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.profesión}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fechaDeEntrega = models.DateTimeField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} {self.fechaDeEntrega} {self.entregado}"


class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"