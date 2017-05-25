from django.db import models
from apps.users.models import usuarios
from django.contrib.auth.models import User

# Create your models here.

class statusSeguidor(models.Model):
	id_statusSeguidor = models.AutoField(primary_key=True, unique=True)
	statusSeguidor = models.CharField(max_length=50)

class seguidores(models.Model):
#	id_seguidor = models.ForeignKey(usuarios, related_name='id_seguidor', null=False, blank=False, on_delete=models.CASCADE)
	id_seguidor = models.ForeignKey(User, related_name='id_seguidor', null=False, blank=False, on_delete=models.CASCADE)
#	id_seguido = models.ForeignKey(usuarios,related_name='id_seguido', null=False, blank=False, on_delete=models.CASCADE)
	id_seguido = models.ForeignKey(User,related_name='id_seguido', null=False, blank=False, on_delete=models.CASCADE)
	id_statusSeguidor1 = models.ForeignKey(statusSeguidor, null=False, blank=False, on_delete=models.CASCADE)

class referidos(models.Model):
#	id_usuarios3 = models.ForeignKey(usuarios, related_name='id_usuarios3', null=False, blank=False, on_delete=models.CASCADE)
	id_usuarios3 = models.ForeignKey(User, related_name='id_usuarios3', null=False, blank=False, on_delete=models.CASCADE)
#	id_referidos = models.ForeignKey(usuarios, related_name='id_referidos', null=False, blank=False, on_delete=models.CASCADE)
	id_referidos = models.ForeignKey(User, related_name='id_referidos', null=False, blank=False, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.id_usuarios3.username

	def save(self,*args,**kwargs):
		uss = self.id_usuarios3
		sub = self.id_referidos
		super(referidos,self).save(*args,**kwargs)

		bus = referidos.objects.filter(id_referidos=uss)
		bu = bus[0].id_usuarios3
		print('AQUI ME VEO MEJOR: %s AQUI EL SUB REFERIDO: %s' %(bu,sub))

		if bus:
			subReferidos.objects.create(id_usuarios9=bu,id_subReferidos=sub)

class subReferidos(models.Model):
#	id_usuarios9 = models.ForeignKey(usuarios, related_name='id_usuarios9', null=False, blank=False, on_delete=models.CASCADE)
	id_usuarios9 = models.ForeignKey(User, related_name='id_usuarios9', null=False, blank=False, on_delete=models.CASCADE)
#	id_subReferidos = models.ForeignKey(usuarios, related_name='id_subReferidos', null=False, blank=False, on_delete=models.CASCADE)
	id_subReferidos = models.ForeignKey(User, related_name='id_subReferidos', null=False, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		return self.id_usuarios9.username

