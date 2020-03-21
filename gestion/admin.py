from django.contrib import admin
from gestion.models import *
# Register your models here.


class profesor_admin(admin.ModelAdmin):
    list_display=("nombres","apellidos","email","nom_usuario","ramos")
    search_fields=("nombres","apellidos","nom_usuario","ramos")


class estudiante_admin(admin.ModelAdmin):
    list_display=("nombres","apellidos","curso")
    search_fields=("nombres","apellidos","curso")
    list_filter=("curso",)

class apoderado_admin(admin.ModelAdmin):
    list_display=("nombres","apellidos","pupilo")
    search_fields=("nombres","apellidos","pupilo")

class cursos_admin(admin.ModelAdmin):
    list_display=("curso","matematica","lenguaje","historia","ciencia","ingles","artes","taller","musica","ed_fisica")
    search_fields=("curso","matematica","lenguaje","historia","ciencia","ingles","artes","taller","musica","ed_fisica")
    list_filter=("curso",)

admin.site.register(Profesor, profesor_admin)
admin.site.register(Estudiante, estudiante_admin)
admin.site.register(Apoderado, apoderado_admin)
admin.site.register(Cursos, cursos_admin)
