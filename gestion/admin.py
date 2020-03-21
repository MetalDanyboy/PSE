from django.contrib import admin
from gestion.models import *
# Register your models here.


class profesor_admin(admin.ModelAdmin):
    list_display=("nombres","apellidos","email","nom_usuario")
    search_fields=("nombres","apellidos","nom_usuario")


class estudiante_admin(admin.ModelAdmin):
    list_display=("nombres","apellidos","curso")
    search_fields=("nombres","apellidos","curso")
    list_filter=("curso",)

class apoderado_admin(admin.ModelAdmin):
    list_display=("nombres","apellidos","pupilo")
    search_fields=("nombres","apellidos","pupilo")

class cursos_admin(admin.ModelAdmin):
    list_display=("curso",)
    search_fields=("curso",)

admin.site.register(Profesor, profesor_admin)
admin.site.register(Estudiante, estudiante_admin)
admin.site.register(Apoderado, apoderado_admin)
admin.site.register(Cursos, cursos_admin)
