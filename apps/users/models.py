from django.db import models
from datetime import datetime

# Create your models here.

class pais(models.Model):
	id_pais = models.AutoField(primary_key=True, unique=True)
	pais = models.CharField(max_length=50)
	def __str__(self):
		return self.pais

class zonaHoraria(models.Model):
	id_zhoraria = models.AutoField(primary_key=True, unique=True)
	zhoraria = models.TimeField()
	def __str__(self):
		return str(self.zhoraria)

class postal(models.Model):
	id_postal = models.AutoField(primary_key=True, unique=True)
	postal = models.IntegerField()
	def __str__(self):
		return str(self.postal)

class nombre(models.Model):
	id_nombre = models.AutoField(primary_key=True, unique=True)
	nombre = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre

class apellido(models.Model):
	id_apellido = models.AutoField(primary_key=True, unique=True)
	apellido = models.CharField(max_length=50)
	def __str__(self):
		return self.apellido

class natalidad(models.Model):
	id_natalidad = models.AutoField(primary_key=True, unique=True)
	natalidad = models.DateField()
	def __str__(self):
		return str(self.natalidad)

class ediPerfil(models.Model):
	id_edPerfil = models.AutoField(primary_key=True, unique=True)
	edPerfil  = models.CharField(max_length=50)
	def __str__(self):
		return self.edPerfil

class nivelUsuario(models.Model):
	id_nivUsuario = models.AutoField(primary_key=True, unique=True)
	nivelUsuario = models.CharField(max_length=50)
	def __str__(self):
		return self.nivelUsuario

class statusUsario(models.Model): 
	id_stusUsuario = models.AutoField(primary_key=True, unique=True)
	stusUsuario = models.CharField(max_length=50)
	def __str__(self):
		return self.stusUsuario

class genero(models.Model):
	id_genero = models.AutoField(primary_key=True, unique=True)
	genero = models.CharField(max_length=50)
	def __str__(self):
		return self.genero

class usuarios(models.Model):
	id_usuarios = models.AutoField(primary_key=True, unique=True)
	usuario = models.CharField(max_length=50)
	correo = models.EmailField()
	contra = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='perfil')
	banner = models.ImageField(upload_to='banner')
	id_zhoraria1 = models.ForeignKey(zonaHoraria, null=False, blank=False, on_delete=models.CASCADE)
	id_pais1 = models.ForeignKey(pais, null=False, blank=False, on_delete=models.CASCADE)
	id_genero1 = models.ForeignKey(genero, null=False, blank=False, on_delete=models.CASCADE)
	id_edperfil1 = models.ForeignKey(ediPerfil, null=False, blank=False, on_delete=models.CASCADE)
	id_postal1 = models.ForeignKey(postal, null=False, blank=False, on_delete=models.CASCADE)
	id_nombre1 = models.ForeignKey(nombre, null=False, blank=False, on_delete=models.CASCADE)
	id_apellido1 = models.ForeignKey(apellido, null=False, blank=False, on_delete=models.CASCADE)
	id_natalidad1 = models.ForeignKey(natalidad, null=False, blank=False, on_delete=models.CASCADE)
	id_nivusuario1 = models.ForeignKey(nivelUsuario, null=False, blank=False, on_delete=models.CASCADE)
	id_stusUsario1 = models.ForeignKey(statusUsario, null=False, blank=False, on_delete=models.CASCADE)
	def __str__(self):
		return self.usuario
#AQUI SE BUSCA SI EL USUARIO TIENE PUNTOS Y SI NO SE LE AGREGAN PARA REGISTRARSE
	def save(self, *args, **kwargs):
		c= self.correo
		u= self.usuario
		super(usuarios, self).save(*args, **kwargs)
		
		for abc in usuarios.objects.filter(correo=c, usuario=u):
			busqueda = puntos.objects.filter(id_usuarios2=abc.id_usuarios).count()
		
			if busqueda == 0:
				puntos.objects.create(id_usuarios2=abc,
										jugadas=0,
										jugadasGanados=0,
										potes=0,
										potesGanados=0,
										quinelas=0,
										quinelasGanadas=0,
										bonusDiario=0,
										promociones=5000,
										referidos=0,
										subReferidos=0,
										enJuego=0,
										regalos=0,
										acumulados=0)
				print('AGREGAR TABLA DE PUNTOS SE ESTA EJECUTANDO')
			else:
				print('YA TIENES UNA TABLA DE PUNTOS')

class puntos(models.Model):
	id_usuarios2 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
	jugadas = models.IntegerField(null=True, blank=True)
	jugadasGanadas = models.IntegerField(null=True, blank=True)
	potes = models.IntegerField(null=True, blank=True)
	potesGanados = models.IntegerField(null=True, blank=True)
	quinelas = models.IntegerField(null=True, blank=True)
	quinelasGanadas = models.IntegerField(null=True, blank=True)
	bonusDiario = models.IntegerField(null=True, blank=True)
	promociones = models.IntegerField(null=True, blank=True)
	referidos = models.IntegerField(null=True, blank=True)
	subReferidos = models.IntegerField(null=True, blank=True)
	enJuego = models.IntegerField(null=True, blank=True)
	regalos = models.IntegerField(null=True, blank=True)
	acumulados = models.IntegerField(null=True, blank=True)

#AQUI SE HACE LA OPERACION PARA DAR EL RESULTADO DE PUNTOSACUMULADOS
	def save(self, *args, **kwargs):
		
		acumulado = ((self.jugadasGanadas + self.potesGanados + self.quinelasGanadas + self.bonusDiario + self.promociones 
					+ self.referidos + self.subReferidos) - self.jugadas - self.potes - self.quinelas - self.enJuego - self.regalos)
		self.acumulados = acumulado
		super(puntos, self).save(*args, **kwargs)
		print('SUMAR PUNTOS SE ESTA EJECUTANDO')






