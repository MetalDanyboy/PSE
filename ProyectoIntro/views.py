from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from gestion.models import Estudiante, Cursos, Profesor
from django.contrib.auth.decorators import login_required

def upper(string):
	return str(string).upper()

def PSE_login(request):
	return render(request, "PSE_login.html")

def PSE_forgotpassword(request):
	return render(request, "PSE_forgotpassword.html")

@login_required
def PSE_profesores(request):
    return render(request, "profesores/PSE_profesores.html")

@login_required
def PSE_profesores_curso_calificaciones(request):
	return render(request, "profesores/PSE_profesores_curso_calificaciones.html")

@login_required
def PSE_profesores_cursos(request):

	nombre_prof=request.user.first_name+' '+request.user.last_name
	profesores=Profesor.objects.all()
	ramos=None
	for profe in profesores:
		if profe.nombres+' '+profe.apellidos == nombre_prof:
			ramos=map(upper,profe.ramos)
	cursos=None
	if(request.GET.get('seleccion')):
		if request.GET.get('seleccion').lower()=='matematica':
			cursos=Cursos.objects.filter(matematica__icontains=nombre_prof)
		elif request.GET.get('seleccion').lower()=='lenguaje':
			cursos=Cursos.objects.filter(lenguaje__icontains=nombre_prof)
		elif request.GET.get('seleccion').lower()=='historia':
			cursos=Cursos.objects.filter(historia__icontains=nombre_prof)
		elif request.GET.get('seleccion').lower()=='ciencia':
			cursos=Cursos.objects.filter(ciencia__icontains=nombre_prof)
		elif request.GET.get('seleccion').lower()=='ingles':
			cursos=Cursos.objects.filter(ingles__icontains=nombre_prof)
		elif request.GET.get('seleccion').lower()=='artes':
			cursos=Cursos.objects.filter(artes__icontains=nombre_prof)
		elif request.GET.get('seleccion').lower()=='taller':
			cursos=Cursos.objects.filter(taller__icontains=nombre_prof)
		elif request.GET.get('seleccion').lower()=='musica':
			cursos=Cursos.objects.filter(musica__icontains=nombre_prof)
		elif request.GET.get('seleccion').lower()=='ed_fisica':
			cursos=Cursos.objects.filter(ed_fisica__icontains=nombre_prof)

	estudiantes=Estudiante.objects.filter()
	return render(request, "profesores/PSE_profesores_cursos.html",{"estudiantes":estudiantes,"cursos":cursos,"ramos":ramos})

@login_required
def PSE_profesores_perfil_profesor(request):
	return render(request, "profesores/PSE_profesores_perfil_profesor.html")

@login_required
def PSE_profesores_alumno(request,user):
	estudiante=Estudiante.objects.filter(id__icontains=user)
	return render(request, "profesores/PSE_profesores_alumno.html",{"estudiante":estudiante})

@login_required
def PSE_profesores_alumno_info(request,user):
	estudiante=Estudiante.objects.filter(id__icontains=user)
	return render(request, "profesores/PSE_profesores_alumno_info.html",{"estudiante":estudiante})

@login_required
def PSE_profesores_alumno_notas(request):
	return render(request, "profesores/PSE_profesores_alumno_notas.html")

@login_required
def PSE_profesores_alumno_progreso(request):
	return render(request, "profesores/PSE_profesores_alumno_progreso.html")

def PSE_test(request):

	estudiantes=Estudiante.objects.filter()

	return render(request, "profesores/test.html",{"estudiantes":estudiantes} )

@login_required
def PSE_obs_por_curso(request):
	return render(request, "profesores/PSE_profesores_observaciones_por_curso.html")
