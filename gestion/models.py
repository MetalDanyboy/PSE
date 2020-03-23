from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.

RAMOS_COLEGIO = (('Matemáticas', 'Matemáticas'),
          ('Lenguaje', 'Lenguaje'),
          ('Historia', 'Historia'),
          ('Ciencia', 'Ciencias'),
          ('Ingles', 'Inglés'),
          ('Artes', 'Artes'),
          ('Taller', 'Taller'),
          ('Musica', 'Música'),
          ('Ed. Fisica', 'Ed. Física'))

class Profesor(models.Model):
    nom_usuario=models.OneToOneField(User, default=1, related_name='profile', primary_key=True, on_delete=models.SET_DEFAULT)
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    fecha_nac=models.DateField(null=True,blank=True)
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=11)
    ramos=MultiSelectField(choices=RAMOS_COLEGIO,default=RAMOS_COLEGIO[0][0])
    foto=models.ImageField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Profesores"

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
    ramos = models.CharField(max_length=50, choices=RAMOS_COLEGIO, default=RAMOS_COLEGIO[0][0])
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ramos+" - "+self.curso.curso+" - "+self.titulo

class Notas(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    assignment = models.ManyToManyField(Assignment)
    nota = models.FloatField()

    class Meta:
        verbose_name_plural = "Notas"

    def evaluacion(self):
        return ",".join([str(p) for p in self.assignment.all()])

    def __str__(self):
        return self.estudiante.nombres+" "+self.estudiante.apellidos