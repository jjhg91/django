from django.db import models
from apps.users.models import usuarios

# Create your models here.

class regalos(models.Model):
	id_regalos = models.IntegerField(primary_key=True)
	regalo = models.CharField(max_length=50)
	puntosNecesarios = models.IntegerField()
	fotoRegalo = models.ImageField(upload_to='img/gift')
	descripcionRegalo = models.CharField(max_length=100)

class statusRegalo(models.Model):
	id_statusRegalo = models.IntegerField(primary_key=True)
	statusRegalo = models.CharField(max_length=50)

class regaloObtenido(models.Model):
	id_usuarios5 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
	id_regalos1 = models.ForeignKey(regalos, null=False, blank=False, on_delete=models.CASCADE)
	id_statusRegalo1 =  models.ForeignKey(statusRegalo, null=False, blank=False, on_delete=models.CASCADE)

