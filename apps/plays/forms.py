from django import forms 
from apps.plays.models import jugadas,partidos
from apps.users.models import puntos
import django

class jugadaForm(forms.ModelForm):
	
	class Meta:
		model = jugadas
#		exclude = ['puntosGanar','fechaJugada','id_rjugada1','id_jugada',]
		fields = ['id_usuarios1','id_partidos1','puntosJugados','jugada',]
		labels = {'id_usuarios1':'usuario','id_partidos1':'partido','puntosJugados':'puntos','jugada':'jugadas',}
		widgets = {'id_usuarios1': forms.NumberInput(attrs={'class':'oculto','readonly':'readonly',}),
					'id_partidos1':forms.NumberInput(attrs={'class':'oculto','readonly':'readonly',}),
					'puntosJugados':forms.TextInput(attrs={'id':'punto',}),
					'jugada':forms.RadioSelect(attrs={'class':'algo',})}
	

	def clean_id_usuarios1(self):
		data = self.cleaned_data['id_usuarios1']
		print('AQUIIIIIIII: %s' %data)
		return data

	def clean_id_partidos1(self):
		data = self.cleaned_data['id_partidos1']
		print('AQUIIIIIIII: %s' %data)
		return data

	def clean_puntosJugados(self):
		data = int(self.cleaned_data['puntosJugados'])
		us = self.cleaned_data['id_usuarios1']
		limite = puntos.objects.filter(id_usuarios2=us).values('acumulados')
		#if limite[0]['acumulados'] < pts:
		limit = int(limite[0]['acumulados'])
		
		print(data)
		print(us)
		print(limite[0]['acumulados'])
		if data > limit:
			raise forms.ValidationError('ESTAS JUGANDO MAS DE LA CUENTA')

		return data

	def clean_id_jugada(self):
		data = self.cleaned_data['id_usuarios1']
		print('AQUIIIIIIII: %s' %data)
		return data