# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
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
                ('id_regalos', models.IntegerField(primary_key=True, serialize=False)),
                ('regalo', models.CharField(max_length=50)),
                ('puntosNecesarios', models.IntegerField()),
                ('fotoRegalo', models.ImageField(upload_to='static/img/gift/')),
                ('descripcionRegalo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='statusRegalo',
            fields=[
                ('id_statusRegalo', models.IntegerField(primary_key=True, serialize=False)),
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
        migrations.AddField(
            model_name='regaloobtenido',
            name='id_usuarios5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usuarios'),
        ),
    ]
