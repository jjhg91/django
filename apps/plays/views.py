from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
# Create your views here.

from apps.plays.models import partidos, jugadas
from apps.plays.forms import jugadaForm

class partid(DetailView):
	template_name = "plays/partido.html"
	model = partidos
	pk_url_kwarg = 'id_partidos'
	context_object_name = 'partido'




class partido(FormView):
	template_name = "plays/partido.html"
	form_class = jugadaForm
	success_url = '/partido/1'
	pk_url_kwarg = 'id_partidos'


	def get_context_data(self,**kwargs):
		context = super(partido,self).get_context_data(**kwargs)
		url_id_partido = self.kwargs['id_partidos']
		context['part'] = partidos.objects.filter(id_partidos=url_id_partido)
		context['jugadas'] = jugadas.objects.filter(id_partidos1=url_id_partido)
		if not context['part']:
			print('NO HAY NADA')

		return context

	def get_initial(self,**kwargs):
		initial = super(partido, self).get_initial()
		initial['id_usuarios1'] = self.request.user.pk
		initial['id_partidos1'] = self.kwargs['id_partidos']
		initial['puntosJugados'] = '1'
		initial['fechaJugada'] = '09/06/1991'
		
		return initial	
	
	def form_valid(self, form):
		print('aqui')
		if form.is_valid():
			jugada = form.save(commit=False)
			#us = form.cleaned_data['id_usuarios1']
			us = self.request.user
			part = self.kwargs['id_partidos']

			jugada.id_usuarios1 = us
			jugada.save()
			print('este es el usuario: %s' %us)
			print('chao')
			

		return super(partido, self).form_valid(form)

#	def form_invalid(self, form):
#
#		print('no paso la prueba')
#		return super(partido, self).form_valid(form)