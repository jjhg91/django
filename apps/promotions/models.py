from django.db import models
from apps.users.models import usuarios
from django.contrib.auth.models import User

# Create your models here.

class bonusDiario(models.Model):
	id_bonusDiario = models.AutoField(primary_key=True, unique=True)
	seguidilla = models.IntegerField()
	puntos = models.IntegerField()

class promociones(models.Model):
	id_promocion = models.AutoField(primary_key=True, unique=True)
	promocion = models.CharField(max_length=50)
	tipoPromocion = models.CharField(max_length=50)
	puntosObtener = models.IntegerField()
	fotoPromocion = models.ImageField(upload_to='img/promotion')

class promoRealizada(models.Model):
#	id_usuarios6 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
	id_usuarios6 = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	id_promocion1 = models.ForeignKey(promociones, null=False, blank=False, on_delete=models.CASCADE)

