from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Profesor(models.Model):
    MY_CHOICES = (('matematica', 'Matematica'),
              ('lenguaje', 'Lenguaje'),
              ('historia', 'Historia'),
              ('ciencia', 'Ciencia'),
              ('ingles', 'Ingles'),
              ('artes', 'Artes'),
              ('taller', 'Taller'),
              ('musica', 'Musica'),
              ('ed_fisica', 'Ed. Fisica'))

    nom_usuario=models.CharField(max_length=50)
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    fecha_nac=models.DateField(null=True,blank=True)
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=11)
    ramos=MultiSelectField(choices=MY_CHOICES,default=MY_CHOICES[0][0])
    foto=models.ImageField(null=True,blank=True)

    def __str__(self):
        return "{} {}".format(self.nombres,self.apellidos)


class Estudiante(models.Model):
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    fecha_nac=models.DateField()
    email_contacto=models.EmailField()
    direccion=models.CharField(max_length=50)
    num_emergencia=models.CharField(max_length=11)
    curso=models.CharField(max_length=2)
    apoderado=models.CharField(max_length=50)
    trastorno=models.CharField(max_length=100)
    observaciones=models.CharField(max_length=500)
    foto=models.ImageField(null=True,blank=True)

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

class Cursos(models.Model):
    curso=models.CharField(max_length=2)
    matematica=models.CharField(max_length=50)
    lenguaje=models.CharField(max_length=50)
    historia=models.CharField(max_length=50)
    ciencia=models.CharField(max_length=50)
    ingles=models.CharField(max_length=50)
    artes=models.CharField(max_length=50)
    taller=models.CharField(max_length=50)
    musica=models.CharField(max_length=50)
    ed_fisica=models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.curso)
