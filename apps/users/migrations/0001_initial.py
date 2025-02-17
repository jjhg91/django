# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 13:07
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='apellido',
            fields=[
                ('id_apellido', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ediPerfil',
            fields=[
                ('id_edPerfil', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('edPerfil', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='natalidad',
            fields=[
                ('id_natalidad', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('natalidad', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='nivelUsuario',
            fields=[
                ('id_nivUsuario', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nivelUsuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='nombre',
            fields=[
                ('id_nombre', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pais',
            fields=[
                ('id_pais', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='postal',
            fields=[
                ('id_postal', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('postal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='puntos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugadas', models.IntegerField(blank=True, null=True)),
                ('jugadasGanadas', models.IntegerField(blank=True, null=True)),
                ('potes', models.IntegerField(blank=True, null=True)),
                ('potesGanados', models.IntegerField(blank=True, null=True)),
                ('quinelas', models.IntegerField(blank=True, null=True)),
                ('quinelasGanadas', models.IntegerField(blank=True, null=True)),
                ('bonusDiario', models.IntegerField(blank=True, null=True)),
                ('promociones', models.IntegerField(blank=True, null=True)),
                ('referidos', models.IntegerField(blank=True, null=True)),
                ('subReferidos', models.IntegerField(blank=True, null=True)),
                ('enJuego', models.IntegerField(blank=True, null=True)),
                ('regalos', models.IntegerField(blank=True, null=True)),
                ('acumulados', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='statusUsario',
            fields=[
                ('id_stusUsuario', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('stusUsuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('foto', models.ImageField(default='perfil/hola.jpg', upload_to='perfil')),
                ('banner', models.ImageField(default='perfil/hola.jpg', upload_to='banner')),
                ('id_apellido1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.apellido')),
                ('id_edperfil1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.ediPerfil')),
                ('id_genero1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.genero')),
                ('id_natalidad1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.natalidad')),
                ('id_nivusuario1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.nivelUsuario')),
                ('id_nombre1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.nombre')),
                ('id_pais1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.pais')),
                ('id_postal1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.postal')),
                ('id_stusUsario1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.statusUsario')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='zonaHoraria',
            fields=[
                ('id_zhoraria', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('zhoraria', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='usuarios',
            name='id_zhoraria1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.zonaHoraria'),
        ),
        migrations.AddField(
            model_name='puntos',
            name='id_usuarios2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
