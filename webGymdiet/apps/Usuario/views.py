from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RegistroForm

# Create your models here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home')

class UserList(ListView):
    model = User
    template_name = 'Usuario/list_user.html'