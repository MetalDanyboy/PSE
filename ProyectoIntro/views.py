from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def PSE_profesores(request):
    return render(request, "PSE_profesores.html")

def PSE_login(request):
	return render(request, "PSE_login.html")

def PSE_forgotpassword(request):
	return render(request, "PSE_forgotpassword.html")