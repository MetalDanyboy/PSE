from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def PSE_login(request):
	return render(request, "PSE_login.html")

def PSE_forgotpassword(request):
	return render(request, "PSE_forgotpassword.html")

def PSE_profesores(request):
    return render(request, "profesores/PSE_profesores.html")

def PSE_profesores_curso_calificaciones(request):
	return render(request, "profesores/PSE_profesores_curso_calificaciones.html")

def PSE_profesores_cursos_1(request):
	return render(request, "profesores/PSE_profesores_cursos_1.html")

def PSE_profesores_perfil_profesor(request):
	return render(request, "profesores/PSE_profesores_perfil_profesor.html")

def PSE_profesores_alumno(request):
	return render(request, "profesores/PSE_profesores_alumno.html")

def PSE_profesores_alumno_info(request):
	return render(request, "profesores/PSE_profesores_alumno_info.html")

def PSE_profesores_alumno_notas(request):
	return render(request, "profesores/PSE_profesores_alumno_notas.html")

def PSE_test(request):
	return render(request, "profesores/PSE_profesores_alumno_notas.html")
