from django.db import models
from django import forms
from .models import Observaciones

class ObservacionesForms(forms.ModelForm):
    class Meta:
        model=Observaciones
        fields=["ramo","observacion"]
