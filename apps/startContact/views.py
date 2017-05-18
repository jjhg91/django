from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from apps.startContact.form import  formlogin
from django.core.urlresolvers import reverse_lazy


class index(FormView):
	form_class = formlogin
	template_name = "index.html"
	success_url = 'admin/'
	#reverse_lazy('index')

	def form_valid(self,form):
		
		if form.is_valid():
			data= form.cleaned_data
			usuario=data['username']
			contra=data['password']
			acceso = authenticate(username=usuario,password=contra)
			print(usuario)
			print(contra)
			if acceso is not None:
				login(self.request,acceso)
			else:
				
				return HttpResponse('usuario no valido')
			
		return super(index, self).form_valid(form)
		
		

