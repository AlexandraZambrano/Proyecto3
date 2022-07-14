from django.db import models


# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f'Profesor {self.id}: {self.nombre} {self.apellido} {self.email}'


class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f'Alumno {self.id}: {self.nombre} {self.apellido} {self.dni} {self.email}'


class Calificaciones(models.Model):
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    notaFinal = models.IntegerField()
    Alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Calificaciones {self.id}: {self.nota1} {self.nota2} {self.notaFinal}'


class Grupo(models.Model):
    turno = models.CharField(max_length=255)
    Alumno = models.ManyToManyField(Alumno)

    def __str__(self):
        return f'Grupo {self.id}: {self.turno}'
