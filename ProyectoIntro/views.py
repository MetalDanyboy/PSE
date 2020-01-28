from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from django.template import loader
from django.shortcuts import render


def PSE(request):
    ahora=datetime.now()
    return render(request, "PSE.html",{"dameFecha":ahora})
