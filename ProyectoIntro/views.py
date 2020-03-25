from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render,redirect
from gestion.models import *
from gestion.forms import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage



def upper(string):
	return str(string).upper()

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
		if profe.nombre == nombre_prof:
			ramos = map(upper,profe.ramos)
	cursos=None

	ramos_minuscula=''
	if  request.GET.get('seleccion'):
		ramos_minuscula = request.GET.get('seleccion').lower()

	if(ramos_minuscula):
		if ramos_minuscula=='matemáticas':
			cursos=Cursos.objects.filter(matematica__icontains=nombre_prof)
		elif ramos_minuscula=='lenguaje':
			cursos=Cursos.objects.filter(lenguaje__icontains=nombre_prof)
		elif ramos_minuscula=='historia':
			cursos=Cursos.objects.filter(historia__icontains=nombre_prof)
		elif ramos_minuscula=='ciencias':
			cursos=Cursos.objects.filter(ciencia__icontains=nombre_prof)
		elif ramos_minuscula=='inglés':
			cursos=Cursos.objects.filter(ingles__icontains=nombre_prof)
		elif ramos_minuscula=='artes':
			cursos=Cursos.objects.filter(artes__icontains=nombre_prof)
		elif ramos_minuscula=='taller':
			cursos=Cursos.objects.filter(taller__icontains=nombre_prof)
		elif ramos_minuscula=='música':
			cursos=Cursos.objects.filter(musica__icontains=nombre_prof)
		elif ramos_minuscula=='ed. física':
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
def PSE_profesores_alumno_notas(request,alumno_id):
	ramos=Ramos.objects.all()
	assignments=Assignment.objects.all()
	profe=request.user.profile
	estudiante=Estudiante.objects.filter(id__icontains=alumno_id)
	notas=Notas.objects.all()

	return render(request, "profesores/PSE_profesores_alumno_notas.html",{"ramos":ramos,
	"assignments":assignments,"estudiante":estudiante,"notas":notas})

@login_required
def PSE_profesores_alumno_progreso(request,alumno_id):
	estudiante=Estudiante.objects.filter(id__icontains=alumno_id)
	obs_alumno=Observaciones.objects.all()
	return render(request, "profesores/PSE_profesores_alumno_progreso.html",{"estudiante":estudiante,"obs_alumno":obs_alumno})

@login_required
def PSE_obs_por_curso(request):
	cursos=Cursos.objects.all()
	nombre_prof=request.user.first_name+" "+request.user.last_name

	lista_cursos_profe=[]
	for curso in cursos:
		if curso.matematica == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.lenguaje == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.historia == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ciencia == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ingles == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.artes == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.taller == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.musica == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ed_fisica == nombre_prof:
			lista_cursos_profe.append(curso.curso)


	curso_selected=""
	if request.GET.get('seleccion_curso'):
		curso_selected = request.GET.get('seleccion_curso')

	alumnos=[]
	if curso_selected:
		alumnos=Estudiante.objects.filter(curso__icontains=curso_selected)

	alumno_selected=""
	if request.GET.get('seleccion_alumno'):
		alumno_selected = request.GET.get('seleccion_alumno')

	form=ObservacionesForms(request.POST or None, )
	if form.is_valid():

		new_form=form.save(commit=False)
		alumno_correcto=Estudiante.objects.filter(
			nombre__icontains=alumno_selected)
		new_form.alumno=alumno_correcto[0]
		new_form.profesor=request.user.profile
		new_form.save()
		form.save_m2m()
		return redirect('obs_por_curso',)
	return render(request, "profesores/PSE_profesores_observaciones_por_curso.html",
	{"cursos":lista_cursos_profe,"curso_selected":curso_selected,"alumnos":alumnos,
	"alumno_selected":alumno_selected,"form":form})

def PSE_profesores_agregar_evaluaciones(request):
	cursos=Cursos.objects.all()
	nombre_prof=request.user.first_name+" "+request.user.last_name

	lista_cursos_profe=[]
	for curso in cursos:
		if curso.matematica == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.lenguaje == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.historia == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ciencia == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ingles == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.artes == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.taller == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.musica == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ed_fisica == nombre_prof:
			lista_cursos_profe.append(curso.curso)

	curso_selected=""
	if request.GET.get('seleccion_curso'):
		curso_selected = request.GET.get('seleccion_curso')

	form=AssignmentForms(request.POST or None, )
	if form.is_valid():
		new_form=form.save(commit=False)
		curso_correcto=Cursos.objects.filter(curso__icontains=curso_selected)
		new_form.curso=curso_correcto[0]
		new_form.profesor=request.user.profile
		new_form.save()
		form.save_m2m()
		return redirect('agregar_evaluaciones',)
	return render(request,"profesores/PSE_profesores_agregar_evaluaciones.html",
	{"cursos":lista_cursos_profe,"curso_selected":curso_selected,"form":form})

def PSE_profesores_agregar_notas(request):
	cursos=Cursos.objects.all()
	nombre_prof=request.user.first_name+" "+request.user.last_name

	lista_cursos_profe=[]
	for curso in cursos:
		if curso.matematica == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.lenguaje == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.historia == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ciencia == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ingles == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.artes == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.taller == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.musica == nombre_prof:
			lista_cursos_profe.append(curso.curso)
		elif curso.ed_fisica == nombre_prof:
			lista_cursos_profe.append(curso.curso)


	curso_selected=""
	if request.GET.get('seleccion_curso'):
		curso_selected = request.GET.get('seleccion_curso')

	alumnos=[]
	if curso_selected:
		alumnos=Estudiante.objects.filter(curso__icontains=curso_selected)

	alumno_selected=""
	if request.GET.get('seleccion_alumno'):
		alumno_selected = request.GET.get('seleccion_alumno')

	form=NotaForms(request.POST or None, )
	if form.is_valid():
		new_form=form.save(commit=False)
		alumno_correcto=Estudiante.objects.filter(
			nombre__icontains=alumno_selected)
		new_form.estudiante=alumno_correcto[0]
		new_form.save()
		form.save_m2m()
		return redirect('agregar_notas',)
	return render(request,"profesores/PSE_profesores_agregar_notas.html",
	{"cursos":lista_cursos_profe,"curso_selected":curso_selected,"alumnos":alumnos,
	"alumno_selected":alumno_selected,"form":form})

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
