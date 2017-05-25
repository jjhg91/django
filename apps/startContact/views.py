#from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from apps.startContact.forms import formlogin, formregistro
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.models import User
from apps.social.models import referidos

class index(FormView):
	form_class = formlogin
	template_name = "startContact/index.html"
	success_url = 'perfi/'
	#reverse_lazy('index')

	def form_valid(self,form):

		if form.is_valid():
			data= form.cleaned_data
			usuario=data['username']
			contra=data['password']
			print(usuario)
			print(contra)

			if '@' in usuario:
				usuario = User.objects.filter(email=usuario).values_list('username')
				
			acceso = authenticate(username=usuario,password=contra)			
			if acceso is not None:
				login(self.request,acceso)
			
			else:
				return HttpResponse('usuario no valido')
			
		return super(index, self).form_valid(form)


class registro(CreateView):
	template_name = 'startContact/registro.html'
	form_class = formregistro
	success_url = reverse_lazy('perfil')

	def get_initial(self,**kwargs):
		initial = super(registro,self).get_initial()
		initial['referido'] = self.kwargs['url_registro']
		return initial

	def form_valid(self,form):
		if form.is_valid():
			usuario = form.save(commit=False)
			refer = form.cleaned_data['referido']
			email = form.cleaned_data['email2']
			userna = form.cleaned_data['username']
			usuario.email = email
			print('chao se comenzo a guardar')
			contra = form.cleaned_data['password2']
			usuario.set_password(contra)
			usuario.save()

			if refer > 0 :
				us = refer
				print(us)
				use = User.objects.get(id=us)
				referido = User.objects.get(email=email)

				print('hola invitado: %s. hola invitador: %s' %(referido,use))
				if use:
					referidos.objects.create(id_usuarios3=use,id_referidos=referido)
					print('tengo un referido: %s' %referido)

			acceso = authenticate(username=userna,password=contra)	
			if acceso is not None:
				login(self.request,acceso)
			

		return super(registro,self).form_valid(form)
		
		

