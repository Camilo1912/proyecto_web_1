from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Ejercicio
from django.urls import reverse_lazy
# Create your views here.


""" class SeccionCreate(CreateView):
    model = Ejercicio
    form_class = SeccionForm
    template_name = 'Registro/agregar_seccion.html'
    success_url = reverse_lazy('secction_list') """

class SeccionList(ListView):
    model = Ejercicio
    template_name = 'Registro/seccion_list.html'

""" class SeccionUpdate(UpdateView):
    model = Ejercicio
    from_class = SeccionForm
    template_name = 'Registro/seccion_form.html'
    success_url = reverse_lazy('secction_list')

class SeccionDelete():
    model = Ejercicio
    form_class = SeccionForm
    template_name = 'Registro/seccion_delete.html'
    success_url = reverse_lazy('secction_list')
 """
#-------------------------------------------------------
