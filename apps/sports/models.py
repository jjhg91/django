from django.db import models

# Create your models here.

class deportes(models.Model):
	id_deportes = models.AutoField(primary_key=True, unique=True)
	deportes = models.CharField(max_length=50)
	foto_d = models.ImageField(upload_to='img/deportes')
	def __str__(self):
		return self.deportes

class ligas(models.Model):
	id_ligas = models.AutoField(primary_key=True, unique=True)
	ligas = models.CharField(max_length=50)
	id_deportes1 = models.ForeignKey(deportes, null=False, blank=False, on_delete=models.CASCADE)
	foto_l = models.ImageField(upload_to='img/ligas')
	def __str__(self):
		return self.ligas

class equipos(models.Model):
	id_equipos = models.AutoField(primary_key=True)
	equipos = models.CharField(max_length=50)
	foto_e = models.ImageField(upload_to='img/equipos')
	ligas1 = models.ManyToManyField(ligas)
	def __str__(self):
			return self.equipos

