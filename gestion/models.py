from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=11)

    def __str__(self):
        return "{} {}".format(self.nombres,self.apellidos)


class Estudiante(models.Model):
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=11)
    curso=models.CharField(max_length=2)
    apoderado=models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.nombres,self.apellidos)

class Apoderado(models.Model):
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=11)
    pupilo=models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.nombres,self.apellidos)
