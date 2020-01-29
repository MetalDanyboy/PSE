from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def PSE_profesores(request):
    return render(request, "PSE_profesores.html")