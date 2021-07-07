from django import forms
from django.db.models.fields import CharField, DateField, TextField
from django.forms import widgets
from .models import *


class SeccionForm(forms.ModelForm):

    class Meta:
        model = Ejercicio
        fields = ['section', 'imagen', 'nombre_ejercicio', 'descripcion1_ejercicio', 'descripcion2_ejercicio', 'pasos']

        labels = {
            'section': 'Sección',
            'imagen': 'Imagen referencial',
            'nombre_ejercicio': 'Nombre del ejercicio',
            'descripcion1_ejercicio': 'Descripción 1',
            'descripcion2_ejercicio': 'Descripción 2',
            'pasos': 'Pasos',
        }

        widgets = {
            'section': forms.Select(choices=SECTION, attrs={'class':'form-control','type':'file'}),
            'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'nombre_ejercicio': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion1_ejercicio': forms.Textarea(attrs={'class': 'form-control'}),
            'descripcion2_ejercicio': forms.Textarea(attrs={'class': 'form-control'}),
            'pasos': forms.Textarea(attrs={'class': 'form-control'}),
        }