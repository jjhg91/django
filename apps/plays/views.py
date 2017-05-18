from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class partido(TemplateView):
	template_name = "partido.html"
