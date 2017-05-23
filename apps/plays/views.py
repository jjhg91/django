from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
# Create your views here.

from apps.plays.models import partidos
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



	def get_initial(self,**kwargs):
		initial = super(partido, self).get_initial()
		initial['id_usuarios1'] = self.request.user
		initial['id_partidos1'] = self.kwargs['id_partidos']
		initial['jugada'] = 3
		initial['puntosJugados'] = 1
		
		initial['fechaJugada'] = '09/06/1991'
		
		return initial

	def get_context_data(self,**kwargs):
		context = super(partido,self).get_context_data(**kwargs)
		url_id_partido = self.kwargs['id_partidos']
		context['part'] = partidos.objects.filter(id_partidos=url_id_partido)
		#print(self.request.user.username)
		return context
	
	
	def form_valid(self, form):
		print('aqui')
		if form.is_valid():
		#	f = form.cleaned_data
		#	u = self.request.user.username
		#	f['id_usuarios1'] = u
		#	f['id_partidos1'] = 1
		#	print(f)
			print('chao')
			form.save(commit=False)

		return super(partido, self).form_valid(form)

	def form_invalid(self, form):

		print('no paso la prueba')
		return super(partido, self).form_valid(form)