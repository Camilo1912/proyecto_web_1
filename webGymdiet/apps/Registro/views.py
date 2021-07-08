from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Ejercicio
from .forms import *
from django.urls import reverse_lazy

from rest_framework import generics
from .serializers import EjercicioSerializer

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
# Create your views here.

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class SeccionCreate(CreateView):
    model = Ejercicio
    form_class = SeccionForm
    template_name = 'Registro/admin_agregar_seccion.html'
    success_url = reverse_lazy('listar_seccion_admin')

class SeccionList(ListView):
    model = Ejercicio
    template_name = 'Registro/ejercicios.html'

class SeccionListAdmin(ListView):
    model = Ejercicio
    template_name = 'Registro/admin_listar_seccion.html'

class SeccionUpdate(UpdateView):
    model = Ejercicio
    from_class = SeccionForm
    template_name = 'Registro/admin_editar_seccion.html'
    success_url = reverse_lazy('listar_seccion')

class SeccionDelete(DeleteView):
    model = Ejercicio
    form_class = SeccionForm
    template_name = 'Registro/admin_eliminar_seccion.html'
    success_url = reverse_lazy('listar_seccion_admin')

#-------------------------------------------------------


class API_objects(generics.ListCreateAPIView):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

#------------------------------------------------------

@api_view(['GET','POST'])
def ejercicio_collection(request):
    if request.method == 'GET':
        ejercicios = Ejercicio.objects.all()
        serializer = EjercicioSerializer(ejercicios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EjercicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

@api_view(['GET', 'PUT', 'DELETE'])
def ejercicio_element(request, pk):
    ejercicio = get_object_or_404(Ejercicio, id=pk)
 
    if request.method == 'GET':
        serializer = EjercicioSerializer(ejercicio)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        ejercicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        ejercicio_new = JSONParser().parse(request) 
        serializer = EjercicioSerializer(ejercicio, data=ejercicio_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

