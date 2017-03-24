from django.db import models
from apps.users.models import usuarios,puntos
from apps.sports.models import deportes,ligas,equipos

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
			
			if self.puntuacion_h  > self.puntuacion_v:
				print('HOME')
				resultado = 2
			elif self.puntuacion_h  == self.puntuacion_v:
				print('EMPATE')
				resultado = 3
			elif self.puntuacion_h  < self.puntuacion_v:
				print('VISITANTE')
				resultado = 4
				
			for jugad in jugadas.objects.filter(id_partidos1 = 1):
				jugad.id_rjugada1.id_rjugada = resultado 
				print(jugad.id_rjugada1.id_rjugada)
				#jugad.save()

			print('UPDATE JUGADAS OCURRIENDO CORRECTAMENTE')

		super(partidos, self).save(*args,*kwargs)


class resultadoJugadas(models.Model):
	id_rjugada = models.AutoField(primary_key=True, unique=True)
	resultadoJ = models.CharField(max_length=50)
	def __str__(self):
		return self.resultadoJ

class jugadas(models.Model):
	id_jugadas = models.AutoField(primary_key=True, unique=True)
	id_usuarios1 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
	id_partidos1 = models.ForeignKey(partidos, null=False, blank=False, on_delete=models.CASCADE)
	puntosJugados = models.IntegerField()
	puntosGanar = models.IntegerField(default=0)
	jugada = models.ForeignKey(resultadoJugadas, related_name='jugada', null=False, blank=False, on_delete=models.CASCADE)
	fechaJugada = models.DateTimeField()
	id_rjugada1 = models.ForeignKey(resultadoJugadas, related_name='id_rjugada1',default=1, null=False, blank=False, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id_jugadas)

	def save(self, *args, **kwargs):

		for instancia in partidos.objects.filter(id_partidos=self.id_partidos1.id_partidos):
			print('pasara algo?',instancia.id_partidos)
			print(self.puntosGanar)
			if self.jugada.id_rjugada == 2 :
				print('HOME1')
				print(self.id_partidos1.home)
				self.puntosGanar = self.puntosJugados * self.id_partidos1.home
				print(self.puntosGanar)
			elif self.jugada.id_rjugada == 3 :
				print('EMPATE2')
				self.puntosGanar = self.puntosJugados * self.id_partidos1.empate
				print(self.puntosGanar)
			elif self.jugada.id_rjugada == 4 :
				print('VISITANTE3')
				self.puntosGanar = self.puntosJugados * self.id_partidos1.visitante
				print(self.puntosGanar)	

			
		if self.id_rjugada1.id_rjugada == 1 :
			todos = self.puntosJugados
		else:
			todos = 0
		ganadas = 0
		i=1
		print('ganar: ',self.puntosGanar, 'jugados: ',self.puntosJugados) 
		for pts in jugadas.objects.filter(id_usuarios1 = self.id_usuarios1.id_usuarios):
			todos = (pts.puntosJugados + todos)			
			if pts.id_rjugada1.id_rjugada == pts.jugada.id_rjugada:
				ganadas = (pts.puntosGanar + ganadas)
			
			if self.id_rjugada1.id_rjugada == 1 and self.id_jugadas == pts.id_jugadas :
				todos = (todos - self.puntosJugados)
				print(i,'hola: ',self.puntosJugados)
				i= i + 1
			if self.id_rjugada1.id_rjugada > 1:			
				if self.id_rjugada1 == self.jugada: 
					if self.id_rjugada1 == pts.jugada and self.id_rjugada1 != pts.id_rjugada1:
						ganadas = (ganadas + self.puntosGanar)
				if self.id_rjugada1 != self.jugada:
					if self.id_rjugada1 != pts.jugada and pts.jugada == pts.id_rjugada1:
						ganadas = (ganadas - self.puntosGanar)

		meterJugadas = puntos.objects.get(id_usuarios2 = self.id_usuarios1.id_usuarios)
		meterJugadas.jugadas = todos
		meterJugadas.jugadasGanadas = ganadas
		print('todo: ',todos)
		print('ganado: ',ganadas)
		meterJugadas.save()


		super(jugadas, self).save(*args,**kwargs)

class pote(models.Model):
	id_pote = models.AutoField(primary_key=True, unique=True)
	id_partidos2 = models.ForeignKey(partidos, null=False, blank=False, on_delete=models.CASCADE)
	nombrePote = models.CharField(max_length=50)
	costePote = models.IntegerField()
	premioPote = models.IntegerField()
	def __str__(self):
		return self.nombrePote

class jugadaPote(models.Model):
	id_usuarios10 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
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
	id_usuarios11 = models.ForeignKey(usuarios, null=False, blank=False, on_delete=models.CASCADE)
	id_porra2 = models.ForeignKey(porra, null=False, blank=False, on_delete=models.CASCADE)
	id_partidos5 = models.ForeignKey(partidos, null=False, blank=False, on_delete=models.CASCADE)
	id_jugadaPorra = models.ForeignKey(resultadoJugadas, null=False, blank=False, on_delete=models.CASCADE)
	