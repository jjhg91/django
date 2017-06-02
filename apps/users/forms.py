from django import forms
from apps.users.models import usuarios, nombre, apellido, postal, natalidad
from PIL import Image
from apps.sports.models import equipos
from django.contrib.admin.widgets import FilteredSelectMultiple

class editarPerfil(forms.ModelForm):
#	deporteFavorito = forms.IntegerField(required=False,label="Deporte Favorito",widget=(forms.NumberInput(attrs={'class':'aqui'})))
#	equiposFavorito = forms.IntegerField(required=True,label="Equipos Favoritos",widget=(forms.NumberInput(attrs={'class':'aqui'})))
	foto = forms.ImageField(required=False)
	banner = forms.ImageField(required=False)
	equiposFavoritos = forms.ModelMultipleChoiceField(queryset=equipos.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
#	destino = forms.MultipleChoiceField(required=False)

	class Meta:
		model = usuarios
		fields = ['foto','banner','id_zhoraria1','equiposFavoritos',]


	def clean_equiposFavoritos(self):
		data = self.cleaned_data['equiposFavoritos']
		print('equipos')
		print(data)
		return data

	def clean_destino(self):
		data = self.cleaned_data['destino']
		print('destino')
		print(data)
		return data

# VALIDANDO EL TAÑAO Y FORMATO DE LA FOTO DE PERFIL
	def clean_foto(self):
		dat = self.cleaned_data['foto']
		kb = 2048 * 1024
		if not dat:
			return dat
		if dat._size < kb:
			end = ('.jpeg','.jpg','.png','.gif')
			if dat.name.endswith(end):
				data = dat
			else:
				raise forms.ValidationError('Formato no permitido')
		else:
			raise forms.ValidationError('Imagen muy pesada')
		
		return data


# VALIDANDO EL TAÑAO Y FORMATO DE LA FOTO DE BANNER
	def clean_banner(self):
		dat = self.cleaned_data['banner']
		kb = 2048 * 1024
		if not dat:
			return dat
		if dat._size < kb:
			end = ('.jpeg','.jpg','.png','.gif')
			if dat.name.endswith(end):
				data = dat
			else:
				raise forms.ValidationError('Formato no permitido')
		else:
			raise forms.ValidationError('Imagen muy pesada')
		
		return data


class informacionPrivada(forms.ModelForm):
	nombre = forms.CharField(required=True,label="Nombre",widget=(forms.TextInput(attrs={'class':'hola'})))
	apellido = forms.CharField(required=True,label="Apellido",widget=(forms.TextInput(attrs={'class':'hola'})))
	postal = forms.CharField(required=True,label="Postal",widget=(forms.TextInput(attrs={'class':'hola'})))
	dia = forms.IntegerField(required=True,label="Dia",widget=(forms.NumberInput(attrs={'class':'hola'})))
	mes = forms.IntegerField(required=True,label="Mes",widget=(forms.NumberInput(attrs={'class':'hola'})))
	año = forms.IntegerField(required=True,label="Año",widget=(forms.NumberInput(attrs={'class':'hola'})))

	class Meta:
		model = usuarios
		fields = ['id_genero1','id_pais1',]
		widgets = {
#			'id_genero1': forms.TextInput(attrs={'class':'hola'}),
#			'id_pais1': forms.TextInput(attrs={'class':'hola'}),
		}

# VALIDO EL NOMBRE
	def clean_nombre(self):
		dat = self.cleaned_data['nombre'].title()
		
		if dat.isalpha():
			busq = nombre.objects.filter(nombre=dat)
			if busq:
				data = busq[0].id_nombre
			else:
				nombre.objects.create(nombre=dat)
				bus = nombre.objects.filter(nombre=dat)
				data = bus[0].id_nombre
		else:
			raise forms.ValidationError('ESTO NO ES LETRA %s' %dat)

		return data


# VALIDO EL APELLIDO 
	def clean_apellido(self):
		dat = self.cleaned_data['apellido'].title()
		
		if dat.isalpha():
			busq = apellido.objects.filter(apellido=dat)
			if busq:
				data = busq[0].id_apellido
			else:
				apellido.objects.create(apellido=dat)
				bus = apellido.objects.filter(apellido=dat)
				data = bus[0].id_apellido
		else:
			raise forms.ValidationError('ESTO NO ES LETRA %s' %dat)

		return data

# VALIDO EL GENERO
	def clean_id_genero1(self):
		data = self.cleaned_data['id_genero1']
	
		return data 

# VALIDO EL PAIS
	def clean_id_pais1(self):
		data = self.cleaned_data['id_pais1']

		return data 

# VALIDO EL CODIGO POSTAL
	def clean_postal(self):
		dat = self.cleaned_data['postal'].upper()
		
		if dat.isalnum():
			busq = postal.objects.filter(postal=dat)
			if busq:
				data = busq[0].id_postal
			else:
				postal.objects.create(postal=dat)
				bus = postal.objects.filter(postal=dat)
				data = bus[0].id_postal
		else:
			raise forms.ValidationError('ESTO NO ES LETRA NI NUMERO: %s' %dat)

		return data


# VALIDO EL DIA 
	def clean_dia(self):
		dat = int(self.cleaned_data['dia'])

		if type(dat) == int :
			if dat <= 31 :
				data = dat
			else:
				raise forms.ValidationError('ESTA NO ES UN DIA DE LA FECHA: %s' %dat)
		else:
			raise forms.ValidationError('ESTA NO ESNUMERO: %s' %dat)

		return data


# VALIDO EL MES
	def clean_mes(self):
		dat = int(self.cleaned_data['mes'])

		if type(dat) == int :
			if dat <= 12 :
				data = dat
			else:
				raise forms.ValidationError('ESTA NO ES UN MES DE LA FECHA: %s' %dat)
		else:
			raise forms.ValidationError('ESTA NO ESNUMERO: %s' %dat)

		return data


# VALIDO SI EL AÑO ES CORRECTO Y INSERTO LA FECHA COMPLETA
	def clean_año(self):
		dat = int(self.cleaned_data['año'])
		
		if type(dat) == int :
			if dat <= 2017 :
				dia = self.cleaned_data['dia']
				mes = self.cleaned_data['mes']
				año = self.cleaned_data['año']
				nacimiento = '%s-%s-%s' %(año,mes,dia)

				busq = natalidad.objects.filter(natalidad=nacimiento)
				if busq:
					data = busq[0].id_natalidad
				else:
					natalidad.objects.create(natalidad=nacimiento)
					bus = natalidad.objects.filter(natalidad=nacimiento)
					data = bus[0].id_natalidad
			else:
				raise forms.ValidationError('ESTA NO ES UN AÑO DE LA FECHA: %s' %dat)
		else:
			raise forms.ValidationError('ESTA NO ESNUMERO: %s' %dat)

		return data 
