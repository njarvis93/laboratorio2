# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-22 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
        ('centrodesalud', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion_sintomas', models.TextField(blank=True, null=True)),
                ('tipo', models.IntegerField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Sucursal')),
            ],
        ),
    ]
