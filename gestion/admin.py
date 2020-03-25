from django.contrib import admin
from gestion.models import *
# Register your models here.

class ramos_admin(admin.ModelAdmin):
    list_display=("ramo",)
    search_fields=("ramo",)

class notas_admin(admin.ModelAdmin):
    list_display=("estudiante","assignment","nota")
    search_fields=("estudiante","assignment","nota")

class assignment_admin(admin.ModelAdmin):
    list_display=("titulo","profesor","ramo","curso")
    search_fields=("titulo","profesor__nombres","profesor__apellidos","ramo","curso__curso")

class profesor_admin(admin.ModelAdmin):
    list_display=("nombre","email","nom_usuario","ramos")
    search_fields=("nombre","nom_usuario","ramos")

class estudiante_admin(admin.ModelAdmin):
    list_display=("nombre","curso")
    search_fields=("nombre","curso")
    list_filter=("curso",)

class cursos_admin(admin.ModelAdmin):
    list_display=("curso","matematica","lenguaje","historia","ciencia","ingles","artes","taller","musica","ed_fisica")
    search_fields=("curso","matematica","lenguaje","historia","ciencia","ingles","artes","taller","musica","ed_fisica")
    list_filter=("curso",)

class observaciones_admin(admin.ModelAdmin):
    list_display=("alumno","profesor","ramo","observacion","fecha_observacion")
    search_fields=("alumno","profesor","ramo","observacion","fecha_observacion")

admin.site.register(Profesor, profesor_admin)
admin.site.register(Estudiante, estudiante_admin)
admin.site.register(Cursos, cursos_admin)
admin.site.register(Notas, notas_admin)
admin.site.register(Assignment, assignment_admin)
admin.site.register(Ramos, ramos_admin)
admin.site.register(Observaciones, observaciones_admin)
