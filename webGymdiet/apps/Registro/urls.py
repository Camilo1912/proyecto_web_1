from django.urls import path, include
from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    path('agregar_seccion', views.SeccionCreate.as_view(), name='crear_seccion'),
    path('listar_seccion', views.SeccionList.as_view(), name='listar_seccion'),
    path('listar_seccion_admin', views.SeccionListAdmin.as_view(), name='listar_seccion_admin'),
    path('editar_seccion/<int:pk>', views.SeccionUpdate.as_view(), name='editar_seccion'),
    path('eliminar_seccion/<int:pk>', views.SeccionDelete.as_view(), name='eliminar_seccion'),

    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),


    path('ejercicios/',  views.ejercicio_collection , name='ejercicio_collection'),
    path('ejercicios/<int:pk>/', views.ejercicio_element ,name='ejercicio_element')
]

