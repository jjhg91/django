from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class ranking(TemplateView):
	template_name = "social/ranking.html"