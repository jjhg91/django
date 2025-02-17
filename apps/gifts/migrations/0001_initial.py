# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regaloObtenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='regalos',
            fields=[
                ('id_regalos', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('regalo', models.CharField(max_length=50)),
                ('puntosNecesarios', models.IntegerField()),
                ('fotoRegalo', models.ImageField(upload_to='img/gift')),
                ('descripcionRegalo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='statusRegalo',
            fields=[
                ('id_statusRegalo', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('statusRegalo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='regaloobtenido',
            name='id_regalos1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifts.regalos'),
        ),
        migrations.AddField(
            model_name='regaloobtenido',
            name='id_statusRegalo1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifts.statusRegalo'),
        ),
    ]
