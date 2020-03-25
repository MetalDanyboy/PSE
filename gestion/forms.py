from django.db import models
from django import forms
from .models import *

class ObservacionesForms(forms.ModelForm):
    class Meta:
        model=Observaciones
        fields=["ramo","observacion"]


class AssignmentForms(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=["titulo","ramo"]

class NotaForms(forms.ModelForm):
    class Meta:
        model=Notas
        fields=["assignment","nota"]
