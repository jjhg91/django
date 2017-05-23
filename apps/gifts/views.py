from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class regalos(TemplateView):
	template_name = "gifts/regalos.html"
