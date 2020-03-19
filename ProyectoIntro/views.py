from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from gestion.models import Estudiante, Cursos

def PSE_login(request):
	return render(request, "PSE_login.html")

def PSE_forgotpassword(request):
	return render(request, "PSE_forgotpassword.html")

def PSE_profesores(request):
    return render(request, "profesores/PSE_profesores.html")

def PSE_profesores_curso_calificaciones(request):
	return render(request, "profesores/PSE_profesores_curso_calificaciones.html")

def PSE_profesores_cursos_1(request):

	cursos=Cursos.objects.filter()
	estudiantes=Estudiante.objects.filter()
	return render(request, "profesores/PSE_profesores_cursos_1.html",{"estudiantes":estudiantes,"cursos":cursos})

def PSE_profesores_perfil_profesor(request):
	return render(request, "profesores/PSE_profesores_perfil_profesor.html")

def PSE_profesores_alumno(request,user):
	estudiante=Estudiante.objects.filter(id__icontains=user)
	return render(request, "profesores/PSE_profesores_alumno.html",{"estudiante":estudiante})

def PSE_profesores_alumno_info(request):
	return render(request, "profesores/PSE_profesores_alumno_info.html")

def PSE_profesores_alumno_notas(request):
	return render(request, "profesores/PSE_profesores_alumno_notas.html")

def PSE_profesores_alumno_progreso(request):
	return render(request, "profesores/PSE_profesores_alumno_progreso.html")

def PSE_test(request):

	estudiantes=Estudiante.objects.filter()

	return render(request, "profesores/test.html",{"estudiantes":estudiantes} )

def PSE_obs_por_curso(request):
	return render(request, "profesores/PSE_profesores_observaciones_por_curso.html")
