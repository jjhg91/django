from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class promociones(TemplateView):
	template_name = "promotions/promociones.html"

class suscripcion(TemplateView):
	template_name = "promotions/suscripcion.html"
