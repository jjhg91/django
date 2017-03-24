from django.db import models

# Create your models here.

class deportes(models.Model):
	id_deportes = models.IntegerField(primary_key=True)
	deportes = models.CharField(max_length=50)
	foto_d = models.ImageField(upload_to='img/equipo')

class ligas(models.Model):
	id_ligas = models.IntegerField(primary_key=True)
	ligas = models.CharField(max_length=50)
	id_deportes1 = models.ForeignKey(deportes, null=False, blank=False, on_delete=models.CASCADE)
	foto_l = models.ImageField(upload_to='img/liga')

class equipos(models.Model):
	id_equipos = models.IntegerField(primary_key=True)
	equipos = models.CharField(max_length=50)
	foto_e = models.ImageField(upload_to='img/equipo')
	ligas1 = models.ManyToManyField(ligas)

