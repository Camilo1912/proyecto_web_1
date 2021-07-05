from django.urls import path, include
from . import views

urlpatterns = [

    path('agregar_seccion', views.SeccionCreate.as_view(), name='crear_seccion'),
    path('listar_seccion', views.SeccionList.as_view(), name='listar_seccion'),
    path('listar_seccion_admin', views.SeccionListAdmin.as_view(), name='listar_seccion_admin'),
    #path('editar_seccion/<int:pk>', views.SeccionUpdate.as_view(), name='editar_seccion'),
    #path('eliminar_seccion/<int:pk>', views.DeleteView.as_view(), name='eliminar_seccion'),
]

