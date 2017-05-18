from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from apps.sports.models import equipos, deportes
# Create your views here.

class inicio(ListView):
	template_name = "inicio.html"
	model = equipos

	def get_context_data(self, **kwargs):
		context = super(inicio, self).get_context_data(**kwargs)
		context['saco'] = deportes.objects.all()
		return context

class deporte(TemplateView):
	template_name = "deporte.html"

class liga(TemplateView):
	template_name = "liga.html"







