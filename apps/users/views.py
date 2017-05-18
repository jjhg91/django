from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.


class perfil(TemplateView):
	template_name = "perfil.html"

class enjuego(TemplateView):
	template_name = "enjuego.html"

class jugadas(TemplateView):
	template_name = "jugadas.html"

class referidos(TemplateView):
	template_name = "referidos.html"
