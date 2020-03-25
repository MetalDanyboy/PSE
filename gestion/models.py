from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

RAMOS_COLEGIO = (('Matemáticas', 'Matemáticas'),
          ('Lenguaje', 'Lenguaje'),
          ('Historia', 'Historia'),
          ('Ciencias', 'Ciencias'),
          ('Inglés', 'Inglés'),
          ('Artes', 'Artes'),
          ('Taller', 'Taller'),
          ('Música', 'Música'),
          ('Ed. Física', 'Ed. Física'))

class Profesor(models.Model):
    nom_usuario=models.OneToOneField(User, default=1, related_name='profile', primary_key=True, on_delete=models.SET_DEFAULT)
    nombre=models.CharField(max_length=200)
    fecha_nac=models.DateField(null=True,blank=True)
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=11)
    ramos=MultiSelectField(choices=RAMOS_COLEGIO,default=RAMOS_COLEGIO[0][0])
    foto=models.ImageField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Profesores"

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre=models.CharField(max_length=200)
    fecha_nac=models.DateField()
    email_contacto=models.EmailField()
    direccion=models.CharField(max_length=50)
    num_emergencia=models.CharField(max_length=11)
    curso=models.CharField(max_length=2)
    apoderado=models.CharField(max_length=50)
    trastorno=models.CharField(max_length=100)
    observacion=models.CharField(max_length=500)
    foto=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.nombre


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

    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return "{}".format(self.curso)

class Ramos(models.Model):
    ramo = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Ramos"

    def __str__(self):
        return self.ramo

class Assignment(models.Model):
    titulo = models.CharField(max_length=50)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    ramo = models.CharField(max_length=50, choices=RAMOS_COLEGIO, default=RAMOS_COLEGIO[0][0])
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ramo+" - "+self.curso.curso+" - "+self.titulo

class Notas(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    assignment = models.ManyToManyField(Assignment)
    nota = models.FloatField()

    class Meta:
        verbose_name_plural = "Notas"

    def evaluacion(self):
        return ",".join([str(p) for p in self.assignment.all()])

    def titulo_nota(self):
        return (",".join([str(p) for p in self.assignment.all()])).split(' - ')[2]

    def curso_nota(self):
        return (",".join([str(p) for p in self.assignment.all()])).split(' - ')[1]

    def ramo_nota(self):
        return (",".join([str(p) for p in self.assignment.all()])).split(' - ')[0]

    def __str__(self):
        return self.estudiante.nombres+" "+self.estudiante.apellidos

class Observaciones(models.Model):
    alumno = models.ForeignKey(Estudiante, on_delete = models.SET_DEFAULT, default = 1)
    profesor = models.ForeignKey(Profesor, on_delete = models.SET_DEFAULT, default = 1)
    observacion = models.TextField()
    fecha_observacion = models.DateField(default=datetime.now)
    ramo = models.CharField(max_length=50, choices=RAMOS_COLEGIO, default=RAMOS_COLEGIO[0][0])

    class Meta:
        verbose_name_plural = "Observaciones"


    def __str__(self):
        return self.alumno.nombres
