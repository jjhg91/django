from django.shortcuts import render
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from apps.users.models import usuarios
from apps.plays.models import jugadas
from apps.social.models import referidos, subReferidos
from apps.users.forms import editarPerfil, informacionPrivada
from django.http import HttpResponseRedirect, HttpResponse
from PIL import Image

class perfil(TemplateView):
	template_name = "users/perfil.html"
	pk_url_kwarg = 'url_perfil'

	def get_context_data(self, **kwargs):
		context = super(perfil, self).get_context_data(**kwargs)
		context['url_perfi'] = int(self.kwargs['url_perfil'])
		context['usuario'] = usuarios.objects.get(id=self.kwargs['url_perfil'])
		return context




def handle_uploaded_file(f,c,w,h):
	with open('C:/Users/JHG/Desktop/desarrolloF/finish/media/%s/%s' %(c,f.name), 'wb+') as destination: 

		for chunk in f.chunks():	
			destination.write(chunk)
	im = Image.open('C:/Users/JHG/Desktop/desarrolloF/finish/media/%s/%s' %(c,f.name))
	
	width = w
	height = h
	im1 = im.resize((width, height), Image.ANTIALIAS)
	im1.save('C:/Users/JHG/Desktop/desarrolloF/finish/media/%s/%s' %(c,f.name))

class editperfil(FormView):
	template_name = 'users/editperfil.html'
	form_class = editarPerfil
	#model = 'usuarios'
	success_url = '..'
	pk_url_kwarg = 'url_perfil'

#	def get_initial(self,**kwargs):
#		initial = super(editperfil,self).get_initial()
#		return initial 

	def get_context_data(self,**kwargs):
		context = super(editperfil, self).get_context_data(**kwargs)
		context['url_perfi'] = int(self.kwargs['url_perfil'])
		return context

	def form_valid(self,form):
		if form.is_valid():
			usuario = self.request.user.id
			foto = form.cleaned_data['foto']
			if foto:
				for ex in foto.name.split('.'):
					if not ex:
						return ext
					extf = ex
				foto.name = '%s.%s'%(self.request.user.pk,extf)
				handle_uploaded_file(foto,'perfil',200,200)
				usuarios.objects.filter(id=usuario).update(foto='perfil/%s'%foto.name)
				foto = "foto='perfil/%s'" %foto.name

			banner = form.cleaned_data['banner']
			if banner:
				for ex in banner.name.split('.'):
					if not ex:
						return ext
					extb = ex
				banner.name = '%s.%s'%(self.request.user.pk,extb)
				handle_uploaded_file(banner,'banner',900,180)
				usuarios.objects.filter(id=usuario).update(banner='banner/%s'%banner.name)
				banner = "banner='banner/%s'"%banner.name

			#return HttpResponse('alfin hizo algo')
			return super(editperfil,self).form_valid(form)






class infpersonal(UpdateView):
	template_name = 'users/infpersonal.html'
	model = usuarios
	form_class = informacionPrivada
	success_url = '/'
	pk_url_kwarg = 'url_perfil'

	def get_initial(self,**kwargs):
		initial = super(infpersonal,self).get_initial()

		return initial

	def get_context_data(self,**kwargs):
		context = super(infpersonal, self).get_context_data(**kwargs)
		context['url_perfi'] = int(self.kwargs['url_perfil'])
		return context

	def form_valid(self,form):
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			apellido = form.cleaned_data['apellido']
			postal = form.cleaned_data['postal']
			genero = form.cleaned_data['id_genero1']
			pais = form.cleaned_data['id_pais1']
			nacimiento = form.cleaned_data['año']
			usuario=self.request.user.id
			usuarios.objects.filter(id=usuario).update(id_nombre1=nombre,
									id_apellido1=apellido,
									id_natalidad1=nacimiento,
									id_genero1=genero,
									id_pais1=pais,)

			return HttpResponse('alfin hizo algo')





class enjuego(TemplateView):
	template_name = "users/enjuego.html"

class jugada(ListView):
	template_name = "users/jugadas.html"
	model = jugadas

	def get_queryset(self,**kwargs):
		usuario = self.kwargs['url_perfil']
		queryset = jugadas.objects.filter(id_usuarios1=usuario)
		return queryset


	def get_context_data(self, **kwargs):
		context = super(jugada, self).get_context_data(**kwargs)
		context['url'] = self.kwargs['url_jugadas']
		context['url_perfi'] = int(self.kwargs['url_perfil'])
		return context



class referido(ListView):
	template_name = "users/referidos.html"
	model = referidos

	def get_queryset(self,**kwargs):
		usuario = self.kwargs['url_perfil']
		queryset = referidos.objects.filter(id_usuarios3=usuario)
		return queryset

	def get_context_data(self, **kwargs):
	    context = super(referido, self).get_context_data(**kwargs)
	    url = self.kwargs['url_referido']
	    context['url_perfi'] = int(self.kwargs['url_perfil'])

	    usuario = self.kwargs['url_perfil']
	    context['subreferidos'] = subReferidos.objects.filter(id_usuarios9=usuario)
	    context['url'] = url

	    return context





from django.core import serializers
from django.http import HttpResponse
from apps.sports.models import deportes,ligas,equipos

class busqueda(TemplateView):
	def get(self, request, *args, **kwargs):

		if request.GET.get('id_deporte'):
			id_deporte = request.GET['id_deporte']
			#respuesta = ligas.objects.filter(id_deportes1__id_deportes=id_deporte)
			respuesta = ligas.objects.all()
			print('AQUI LAS LIGAS: %s' %respuesta[0].id_ligas)
			data = serializers.serialize('json',respuesta,fields=('ligas'))
			print('AQUI LAS LIGAS: %s' %data)
		
		if request.GET.get('id_liga'):
			id_liga = request.GET['id_liga']
			print(type(id_liga))
			print(id_liga)
			print('POR AQUI ESTOYy')
			respuesta = equipos.objects.filter(ligas1__pk=id_liga)
			data = serializers.serialize('json',respuesta,fields=('equipos','ligas1'))
		

		mimetype='application/json'
		return HttpResponse(data,mimetype)

