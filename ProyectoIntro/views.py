from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from gestion.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

def upper(string):
	return str(string).upper()

"""def PSE_login(request):
	return render(request, "PSE_login.html")""" #ESTO NO ERA NECESARIO

def PSE_forgotpassword(request):
	return render(request, "PSE_forgotpassword.html")

@login_required
def PSE_profesores(request):
    return render(request, "profesores/PSE_profesores.html")

@login_required
def PSE_profesores_curso_calificaciones(request):
	"""if request.method == 'POST' and request.FILES['notas']:
		notas = request.FILES['notas']
		fs = FileSystemStorage()
		filename = fs.save(notas.name, notas)
		uploaded_file_url = fs.url(filename)
		return render(request, 'profesores/PSE_profesores_curso_calificaciones.html', {'uploaded_file_url': uploaded_file_url})"""
	return render(request, "profesores/PSE_profesores_curso_calificaciones.html")

@login_required
def PSE_profesores_cursos(request):

	nombre_prof=request.user.first_name+' '+request.user.last_name
	profesores=Profesor.objects.all()
	ramos=None
	for profe in profesores:
		if profe.nombres+' '+profe.apellidos == nombre_prof:
			ramos = map(upper,profe.ramos)
	cursos=None

	ramos_minuscula=''
	if  request.GET.get('seleccion'):
		ramos_minuscula = request.GET.get('seleccion').lower()

	if(ramos_minuscula):
		if ramos_minuscula=='matematica':
			cursos=Cursos.objects.filter(matematica__icontains=nombre_prof)
		elif ramos_minuscula=='lenguaje':
			cursos=Cursos.objects.filter(lenguaje__icontains=nombre_prof)
		elif ramos_minuscula=='historia':
			cursos=Cursos.objects.filter(historia__icontains=nombre_prof)
		elif ramos_minuscula=='ciencia':
			cursos=Cursos.objects.filter(ciencia__icontains=nombre_prof)
		elif ramos_minuscula=='ingles':
			cursos=Cursos.objects.filter(ingles__icontains=nombre_prof)
		elif ramos_minuscula=='artes':
			cursos=Cursos.objects.filter(artes__icontains=nombre_prof)
		elif ramos_minuscula=='taller':
			cursos=Cursos.objects.filter(taller__icontains=nombre_prof)
		elif ramos_minuscula=='musica':
			cursos=Cursos.objects.filter(musica__icontains=nombre_prof)
		elif ramos_minuscula=='ed_fisica':
			cursos=Cursos.objects.filter(ed_fisica__icontains=nombre_prof)

	estudiantes=Estudiante.objects.filter()
	return render(request, "profesores/PSE_profesores_cursos.html",{"estudiantes":estudiantes,"cursos":cursos,"ramos":ramos})

@login_required
def PSE_profesores_perfil_profesor(request):
	return render(request, "profesores/PSE_profesores_perfil_profesor.html",{"profesor":request.user.profile})

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
	ramos=Ramos.objects.all()
	assignments=Assignment.objects.all()
	profe=request.user.profile

	print(assignments[0].profesor)
	print(ramos)

	return render(request, "profesores/PSE_profesores_alumno_notas.html",{"ramos":ramos,"assignments":assignments})

@login_required
def PSE_profesores_alumno_progreso(request):
	return render(request, "profesores/PSE_profesores_alumno_progreso.html")

@login_required
def PSE_obs_por_curso(request):
	return render(request, "profesores/PSE_profesores_observaciones_por_curso.html")




#-------------------Usar solo para Pruebas-------------------------


def PSE_test(request):
	nombre_prof=request.user.first_name+' '+request.user.last_name
	profesores=Profesor.objects.all()
	ramos=None
	for profe in profesores:
		if profe.nombres+' '+profe.apellidos == nombre_prof:
			ramos = map(upper,profe.ramos)
	cursos=None

	ramos_minuscula=''
	if  request.GET.get('seleccion'):
		ramos_minuscula = request.GET.get('seleccion').lower()

	if(ramos_minuscula):
		if ramos_minuscula=='matematica':
			cursos=Cursos.objects.filter(matematica__icontains=nombre_prof)
		elif ramos_minuscula=='lenguaje':
			cursos=Cursos.objects.filter(lenguaje__icontains=nombre_prof)
		elif ramos_minuscula=='historia':
			cursos=Cursos.objects.filter(historia__icontains=nombre_prof)
		elif ramos_minuscula=='ciencia':
			cursos=Cursos.objects.filter(ciencia__icontains=nombre_prof)
		elif ramos_minuscula=='ingles':
			cursos=Cursos.objects.filter(ingles__icontains=nombre_prof)
		elif ramos_minuscula=='artes':
			cursos=Cursos.objects.filter(artes__icontains=nombre_prof)
		elif ramos_minuscula=='taller':
			cursos=Cursos.objects.filter(taller__icontains=nombre_prof)
		elif ramos_minuscula=='musica':
			cursos=Cursos.objects.filter(musica__icontains=nombre_prof)
		elif ramos_minuscula=='ed_fisica':
			cursos=Cursos.objects.filter(ed_fisica__icontains=nombre_prof)

	estudiantes=Estudiante.objects.filter()
	return render(request, "profesores/test.html",{"estudiantes":estudiantes,"cursos":cursos,"ramos":ramos})
