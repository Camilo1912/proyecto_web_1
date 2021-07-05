from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Ejercicio
from .forms import *
from django.urls import reverse_lazy
# Create your views here.


class SeccionCreate(CreateView):
    model = Ejercicio
    form_class = SeccionForm
    template_name = 'Registro/agregar_seccion.html'
    success_url = reverse_lazy('listar_seccion_admin')

class SeccionList(ListView):
    model = Ejercicio
    template_name = 'Registro/ejercicios.html'

class SeccionListAdmin(ListView):
    model = Ejercicio
    template_name = 'Registro/listar_seccion.html'

""" class SeccionUpdate(UpdateView):
    model = Ejercicio
    from_class = SeccionForm
    template_name = 'Registro/seccion_form.html'
    success_url = reverse_lazy('listar_seccion') """

""" class SeccionDelete():
    model = Ejercicio
    form_class = SeccionForm
    template_name = 'Registro/seccion_delete.html'
    success_url = reverse_lazy('listar_seccion') """

#-------------------------------------------------------
