# Generated by Django 3.2.4 on 2021-06-25 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_auto_20210624_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejercicio',
            name='section',
            field=models.CharField(choices=[('ABDOMEN', 'ABDOMEN'), ('ESPALDA', 'ESPALDA'), ('PECHO', 'PECHO'), ('BRAZO', 'BRAZO')], default='ABDOMEN', max_length=15),
        ),
    ]