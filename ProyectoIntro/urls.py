"""ProyectoIntro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoIntro.views import *

urlpatterns = [
    path('test/', PSE_test, name = "test"),
    path('admin/', admin.site.urls, name = "admin"),
    path('profesores/',PSE_profesores, name = "profesores"),
    path('', PSE_login, name = "login"),
    path('forgotpassword/', PSE_forgotpassword, name = "forgotpassword"),
    path('profesores/cursos/', PSE_profesores_cursos_1, name = "cursos_1"),
    path('profesores/cursos/calificaciones',PSE_profesores_curso_calificaciones, name = "curso_calificaciones"),
    path('profesores/alumno/<user>', PSE_profesores_alumno, name = "alumno"),
    path('profesores/alumno/notas/', PSE_profesores_alumno_notas, name = "alumno_notas"),
    path('profesores/alumno/info/<user>', PSE_profesores_alumno_info, name = "alumno_info"),
    path('profesores/alumno/progreso/', PSE_profesores_alumno_progreso, name = "alumno_progreso"),
    path('profesores/perfil', PSE_profesores_perfil_profesor, name = "perfil_profesor"),
    path('profesores/obs_curso', PSE_obs_por_curso, name = "obs_por_curso")
]
