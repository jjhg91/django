from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from apps.plays.models import jugadas
from apps.social.models import referidos, subReferidos


class perfil(TemplateView):
	template_name = "users/perfil.html"

class enjuego(TemplateView):
	template_name = "users/enjuego.html"

class jugada(ListView):
	template_name = "users/jugadas.html"
	model = jugadas

	def get_queryset(self,**kwargs):
		usuario = self.request.user
		queryset = jugadas.objects.filter(id_usuarios1=usuario)
		return queryset


	def get_context_data(self, **kwargs):
		context = super(jugada, self).get_context_data(**kwargs)
		context['url'] = url = self.kwargs['url_jugadas']
		return context



class referido(ListView):
	template_name = "users/referidos.html"
	model = referidos

	def get_queryset(self,**kwargs):
		usuario = self.request.user
		queryset = referidos.objects.filter(id_usuarios3=usuario)
		return queryset

	def get_context_data(self, **kwargs):
	    context = super(referido, self).get_context_data(**kwargs)
	    url = self.kwargs['url_referido']
	    usuario = self.request.user
	    context['sub'] = subReferidos.objects.filter(id_usuarios9=usuario)
	    context['url'] = url
	    return context