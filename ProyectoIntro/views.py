from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #primera vista
    persona1=Persona("Daniel","Sepúlveda")
    ahora=datetime.now()

    """doc_externo=open("C:/Users/Familia/Documents/ProyectoDjango/ProyectoIntro/ProyectoIntro/plantillas/miPlantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()"""


    #doc_externo=loader.get_template('miPlantilla.html') #esta linea reemplaza las comentadas arriba

    users=["Admin","Profesores","Alumnos"]

    """ctx=Context({"nombre_persona":persona1.nombre,"apellido_persona":persona1.apellido,"fecha":ahora,\
     "usuarios":users})"""

    #ctx={"nombre_persona":persona1.nombre,"apellido_persona":persona1.apellido,"fecha":ahora,\
    # "usuarios":users} #cuando usamos el loader el ctx tiene que ser directamente un diccionario

    #documento=doc_externo.render(ctx)


    #return HttpResponse(documento)

    return render(request, "miPlantilla.html",{"nombre_persona":persona1.nombre,"apellido_persona":persona1.apellido,"fecha":ahora,\
      "usuarios":users})

def despedida(request):
    return HttpResponse("Hasta luego!!")

def calculaEdad(request,edad,anno):
    periodo=anno-2020
    edadFutura=edad+periodo

    documento="<html><body> <h2> en el año %s tendrás %s años</h2></body></html>" %(anno,edadFutura)
    return HttpResponse(documento)
def PSE(request):
    ahora=datetime.now()
    return render(request, "PSE.html",{"dameFecha":ahora})
