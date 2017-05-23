from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from apps.sports.models import equipos, deportes, ligas
from apps.plays.models import partidos

#from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

class inicio(ListView):
	template_name = "sports/inicio.html"
	model = equipos
	#queryset = equipos.objects.filter(equipos='barcelona')
	def get_context_data(self, **kwargs):
		context = super(inicio, self).get_context_data(**kwargs)
		context['saco'] = deportes.objects.all()
		return context

	
#from django.shortcuts import get_object_or_404

class deporte(ListView):
	template_name = "sports/deporte.html"
	model = partidos


	def get_queryset(self,**kwargs):
		part = self.kwargs['url_deporte']
		queryset = partidos.objects.filter(id_ligas2__id_deportes1__id_deportes=part)
		return queryset


	def get_context_data(self,**kwargs):
		context = super(deporte, self).get_context_data(**kwargs)
		context['liga'] = ligas.objects.filter(id_deportes1 = self.kwargs['url_deporte'])
		context['object'] = self.object_list
		if not context['object']:
			context['msj'] = 'Elegir un deporte por favor'
	
		return context




#	def get(self, request, *args, **kwargs):
#		part = int(self.kwargs['hii'])
#		if part < 2:
#			return HttpResponse('Hello, World! %s' %part)
#		else:
#			return HttpResponse('aqui %s' %part)
		


class liga(ListView):
	template_name = "sports/liga.html"
	model = partidos

	def get_queryset(self,**kwargs):
		lig = self.kwargs['url_liga']
		queryset = partidos.objects.filter(id_ligas2=lig)
		return queryset


	def get_context_data(self, **kwargs):
		context = super(liga, self).get_context_data(**kwargs)
		li = self.kwargs['url_liga']
		context['equipo'] = equipos.objects.filter(ligas1=li)
		return context





