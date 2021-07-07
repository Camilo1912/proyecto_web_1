from django.db import models
from django.db.models.fields.files import ImageField


SECTION = (
    ('NONE','NONE'),
    ('ABDOMEN','ABDOMEN'),
    ('ESPALDA','ESPALDA'),
    ('PECHO','PECHO'),
    ('BRAZO','BRAZO'),
)
    

class Ejercicio(models.Model):
    section = models.CharField(max_length=15, choices=SECTION, default='NONE')
    imagen = models.ImageField(upload_to='ejerciciofoto')
    nombre_ejercicio = models.CharField(max_length=30)
    descripcion1_ejercicio = models.TextField(default='no info')
    descripcion2_ejercicio = models.TextField(default='no info')
    pasos = models.TextField()
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre_ejercicio


