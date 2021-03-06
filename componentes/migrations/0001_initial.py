# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correoElectronico', models.CharField(max_length=50)),
                ('texto', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Independiente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('aniosExperiencia', models.IntegerField()),
                ('foto', models.CharField(max_length=1000)),
                ('telefono', models.IntegerField()),
                ('correoElectronico', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=15)),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='independiente',
            name='idServicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componentes.Servicio'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='idIdependiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componentes.Independiente'),
        ),
    ]
