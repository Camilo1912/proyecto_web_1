# Generated by Django 3.2.4 on 2021-06-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_auto_20210624_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejercicio',
            name='descripcion_ejercicio',
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='descripcion1_ejercicio',
            field=models.TextField(default='no info'),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='descripcion2_ejercicio',
            field=models.TextField(default='no info'),
        ),
    ]
