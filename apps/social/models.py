from django.db import models
from apps.users.models import usuarios

# Create your models here.

class statusSeguidor(models.Model):
	id_statusSeguidor = models.AutoField(primary_key=True, unique=True)
	statusSeguidor = models.CharField(max_length=50)

class seguidores(models.Model):
	id_seguidor = models.ForeignKey(usuarios, related_name='id_seguidor', null=False, blank=False, on_delete=models.CASCADE)
	id_seguido = models.ForeignKey(usuarios,related_name='id_seguido', null=False, blank=False, on_delete=models.CASCADE)
	id_statusSeguidor1 = models.ForeignKey(statusSeguidor, null=False, blank=False, on_delete=models.CASCADE)

class referidos(models.Model):
	id_usuarios3 = models.ForeignKey(usuarios, related_name='id_usuarios3', null=False, blank=False, on_delete=models.CASCADE)
	id_referidos = models.ForeignKey(usuarios, related_name='id_referidos', null=False, blank=False, on_delete=models.CASCADE)

class subReferidos(models.Model):
	id_usuarios9 = models.ForeignKey(usuarios, related_name='id_usuarios9', null=False, blank=False, on_delete=models.CASCADE)
	id_subReferidos = models.ForeignKey(usuarios, related_name='id_subReferidos', null=False, blank=False, on_delete=models.CASCADE)


