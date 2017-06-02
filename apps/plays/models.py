from django.db import models
from django.db.models import F,Sum,Count
from apps.users.models import usuarios,puntos
from apps.sports.models import deportes,ligas,equipos
from django.contrib.auth.models import User
from datetime import datetime   

# Create your models here.

class partidos(models.Model):
	id_partidos = models.AutoField(primary_key=True, unique=True)
	id_equiposh = models.ForeignKey(equipos, related_name='equiposh', null=False, blank=False, on_delete=models.CASCADE)
	id_equiposv = models.ForeignKey(equipos, related_name='equiposv', null=False, blank=False, on_delete=models.CASCADE)
	id_ligas2 = models.ForeignKey(ligas, null=False, blank=False, on_delete=models.CASCADE)
	fecha = models.DateTimeField()
	home = models.DecimalField(max_digits=3, decimal_places=2)
	empate = models.DecimalField(max_digits=3, decimal_places=2)
	visitante = models.DecimalField(max_digits=3, decimal_places=2)
	puntuacion_h = models.IntegerField(default=0)
	puntuacion_v = models.IntegerField(default=0)
	actualizado = models.IntegerField(default=1)
	def __str__(self):
		return str(self.id_partidos)

	def save(self, *args, **kwargs):
		if self.actualizado == 2:
#VER CUAL EQUIPO RESULTO GANADOR PARA GUARDAR EN VARIABLE RESULTADO	
			if self.puntuacion_h  > self.puntuacion_v:
				print('HOME')
				resultado = 2
			elif self.puntuacion_h  == self.puntuacion_v:
				print('EMPATE')
				resultado = 3
			elif self.puntuacion_h  < self.puntuacion_v:
				print('VISITANTE')
				resultado = 4
#UPDATE DE PARTIDOS EN LA TABLA JUGADAS 
			jugadas.objects.filter(id_partidos1 = self.id_partidos).update(id_rjugada1=resultado)
#UPDATE DE JUGADASGANADAS EN TABLA PUNTOS PARA LA SUMA DE PUNTOS ACUMULADOS
			for hola in jugadas.objects.filter(id_partidos1__id_partidos=self.id_partidos).values('id_usuarios1').annotate(sumar=Sum('id_usuarios1')):
#				busca = jugadas.objects.filter(id_usuarios1__id_usuarios = hola['id_usuarios1'], jugada__id_rjugada=F('id_rjugada1__id_rjugada')).values('id_usuarios1').annotate(total=Sum('puntosGanar'))
				busca = jugadas.objects.filter(id_usuarios1__username = hola['id_usuarios1'], jugada__id_rjugada=F('id_rjugada1__id_rjugada')).values('id_usuarios1').annotate(total=Sum('puntosGanar'))
				print('hola: ',hola['id_usuarios1'])
				print('busca: ',busca[0]['total'])
#				put=puntos.objects.get(id_usuarios2__id_usuarios = hola['id_usuarios1'])
				put=puntos.objects.get(id_usuarios2__username = hola['id_usuarios1'])
				put.jugadasGanadas = busca[0]['total']
				put.save()
				
			print('UPDATE JUGADAS OCURRIENDO CORRECTAMENTE')

		super(partidos, self).save(*args,*kwargs)



class resultadoJugadas(models.Model):
	id_rjugada = models.AutoField(primary_key=True, unique=True)
	resultadoJ = models.CharField(max_length=50)
	def __str__(self):
		return self.resultadoJ

class jugadas(models.Model):
	id_jugadas = models.AutoField(primary_key=True, unique=True)
#	id_usuarios1 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
	id_usuarios1 = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	id_partidos1 = models.ForeignKey(partidos, null=False, blank=False, on_delete=models.CASCADE)
	puntosJugados = models.IntegerField()
	puntosGanar = models.IntegerField(default=0)
	jugada = models.ForeignKey(resultadoJugadas, related_name='jugada', null=False, blank=False, on_delete=models.CASCADE)
	fechaJugada = models.DateTimeField(default=datetime.now)
	id_rjugada1 = models.ForeignKey(resultadoJugadas, related_name='id_rjugada1',default=1, null=False, blank=False, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id_jugadas)

	def save(self, *args, **kwargs):
#MULTIPLICANDO LOS PUNTOS JUGADOS POR EL PORCENTAJE DE PREMIACION
		for instancia in partidos.objects.filter(id_partidos=self.id_partidos1.id_partidos):
			if self.jugada.id_rjugada == 2 :
				print('HOME')
				self.puntosGanar = self.puntosJugados * self.id_partidos1.home
				print('GANAR: ',self.puntosGanar)
			elif self.jugada.id_rjugada == 3 :
				print('EMPATE')
				self.puntosGanar = self.puntosJugados * self.id_partidos1.empate
				print('GANAR: ',self.puntosGanar)
			elif self.jugada.id_rjugada == 4 :
				print('VISITANTE')
				self.puntosGanar = self.puntosJugados * self.id_partidos1.visitante
				print('GANAR: ',self.puntosGanar)	

		super(jugadas, self).save(*args,**kwargs)
#ACTUALIZANDO LA TABLA PUNTOS CON LAS JUGADAS HECHAS
		ho=jugadas.objects.filter(id_usuarios1= self.id_usuarios1).values('id_usuarios1').annotate(jugadas=Sum('puntosJugados'))
		print(ho)
		ptsJ=puntos.objects.get(id_usuarios2= self.id_usuarios1)
		ptsJ.jugadas=ho[0]['jugadas']
		ptsJ.save()		

class pote(models.Model):
	id_pote = models.AutoField(primary_key=True, unique=True)
	id_partidos2 = models.ForeignKey(partidos, null=False, blank=False, on_delete=models.CASCADE)
	nombrePote = models.CharField(max_length=50)
	costePote = models.IntegerField()
	premioPote = models.IntegerField()
	def __str__(self):
		return self.nombrePote

class jugadaPote(models.Model):
#	id_usuarios10 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
	id_usuarios10 = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	id_pote1 = models.ForeignKey(pote, null=False, blank=False, on_delete=models.CASCADE)
	resultadoHPote = models.IntegerField()
	resultadoVPote = models.IntegerField()
	fechaPote = models.DateTimeField()
	id_resultadoPote1 = models.ForeignKey(resultadoJugadas, null=False, blank=False, on_delete=models.CASCADE)

class porra(models.Model):
	id_porra = models.AutoField(primary_key=True, unique=True)
	nombrePorra = models.CharField(max_length=100)
	premioPorra = models.IntegerField()
	def __str__(self):
		return self.nombrePorra

class porraEquipos(models.Model):
	id_porra4 = models.ForeignKey(porra, null=False, blank=False, on_delete=models.CASCADE)
	id_partidos4 = models.ForeignKey(partidos, null=False, blank=False, on_delete=models.CASCADE)
	id_rjugada = models.ForeignKey(resultadoJugadas, null=False, blank=False, on_delete=models.CASCADE)

class jugadaPorra(models.Model):
#	id_usuarios11 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
	id_usuarios11 = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	id_porra2 = models.ForeignKey(porra, null=False, blank=False, on_delete=models.CASCADE)
	id_partidos5 = models.ForeignKey(partidos, null=False, blank=False, on_delete=models.CASCADE)
	id_jugadaPorra = models.ForeignKey(resultadoJugadas, null=False, blank=False, on_delete=models.CASCADE)
	