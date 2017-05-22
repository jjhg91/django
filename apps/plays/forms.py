from django import forms 
from apps.plays.models import jugadas,partidos


class jugadaForm(forms.ModelForm):
	
	class Meta:
		model = jugadas
#		exclude = ['puntosGanar','fechaJugada','id_rjugada1','id_jugada',]
		fields = ['id_usuarios1','id_partidos1','puntosJugados','jugada','fechaJugada',]
		labels = {'id_usuarios1':'usuario','id_partidos1':'partido','puntosJugados':'puntos','jugada':'jugada',}
#		widgets = {'id_usuarios1': forms.NumberInput(attrs={'class':'algo',}),
#					'id_partidos1':forms.NumberInput(attrs={'class':'algo',}),
#					'puntosJugados':forms.NumberInput(attrs={'class':'algo',}),
#					'jugada':forms.NumberInput(attrs={'class':'algo',}),
#					'fechaJugada':forms.DateInput(attrs={'class':'algo',}),}
	

	def clean_id_partidos1(self):
	
		#u = self.cleaned_data['id_usuarios1']
		
		pass