from django import forms
from django.contrib.auth.models import User
from apps.users.models import usuarios


# FORMUARIO DE REGISTRO

class formregistro(forms.ModelForm):
	referido = forms.IntegerField(required=True,label="referido",widget=(forms.NumberInput(attrs={'readonly':'readonly'})))
	password2 = forms.CharField(max_length=20,required=True,label="Password2",widget=(forms.PasswordInput(attrs={'id':'password2'})))
	email2 = forms.CharField(max_length=20,required=True,label="Email2",widget=(forms.EmailInput(attrs={'id':'email2'})))
	
	class Meta:
		model = usuarios
		fields = ['username','email','password','id_pais1','id_zhoraria1','id_genero1',]
		widgets = {
			'username': forms.TextInput(attrs={'id':'text'}),
			'email': forms.EmailInput(attrs={'id':'email'}),
			'password': forms.PasswordInput(attrs={'id':'password'}),
			'id_pais1': forms.Select(attrs={'id':'pais'}),
			'id_zhoraria1': forms.Select(attrs={'id':'zhoraria'}),
			'id_genero1': forms.RadioSelect(attrs={'id':'genero'}),
		}


	# VERIFICAMOS EL USERNAME

	def clean_username(self):
		data = self.cleaned_data['username']
		print('username: %s'%data)
		if len(data) > 30:
			raise forms.ValidationError('USUARIO MUY LARGO')

		def nopermitido(v):
			nopermitido = ['/','\ ','"',"'"]
			n=0
			
			for letra in v:
				for st in nopermitido:
					if st == letra:
						n = n + 1
			
			if n > 0: 	
				raise forms.ValidationError('CARACTERES NO PERMITIDOS')
		

		nopermitido(data)

		return data


	# VERIFICAMOS EL EMAIL

	def clean_email2(self):
		email = self.cleaned_data['email']
		email2 = self.cleaned_data['email2']

		if not email2 == email:
			raise forms.ValidationError('TU CORREO NO COINSIDE ESCRIBELO EXACTAMENTE IGUAL')
		data = email2
		print('email: %s' %data)
		if len(data) > 30:
			raise forms.ValidationError('EMAIL MUY LARGO')

		def nopermitido(v):
			nopermitido = ['/','\ ','"',"'"]
			n=0
			
			for letra in v:
				for st in nopermitido:
					if st == letra:
						n = n + 1
			
			if n > 0: 	
				raise forms.ValidationError('CARACTERES NO PERMITIDOS')

		def contarArrobaPunto(data,buscar):
			
			if buscar == '.':
				a,b = data.split('@')
				data = b

			if not buscar in data:
				raise forms.ValidationError('NO TIENE %s' %buscar )

			r = 0
			for letra in data:
				if letra == buscar:
					r = r+1
					if r > 1:
						raise forms.ValidationError('TIENE MAS DE UN %s' %buscar )
		
		nopermitido(data)
		contarArrobaPunto(data,'@')
		contarArrobaPunto(data,'.')

		
		
		return data


	# VERIFICAMOS EL PASSWORD

	def clean_password2(self):
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if not  password2 == password:
			raise forms.ValidationError('PASSWORDS NO COINCIDEN')
		data = password2
		print('password: %s' %data)

		def nopermitido(v):
			nopermitido = ['/','\ ','"',"'"]
			n=0
			
			for letra in v:
				for st in nopermitido:
					if st == letra:
						n = n + 1
			
			if n > 0: 	
				raise forms.ValidationError('CARACTERES NO PERMITIDOS')

		nopermitido(data)
		return data


	#VERIFICAMOS EL PAIS

	def clean_id_pais1(self):
		data = self.cleaned_data['id_pais1']
		print('pais: %s' %data)

		return data


	# VERIFICAMOS ZONA HORARIA

	def clean_id_zhoraria1(self):
		data = self.cleaned_data['id_zhoraria1']
		print('horario: %s' %data)

		return data


	# VERIFICAMOS EL GENERO

	def clean_id_genero1(self):
		data = self.cleaned_data['id_genero1']
		print('genero: %s' %data)

		return data

	# VERIFICAR REFERIDOS

	def clean_referido(self):
		data = self.cleaned_data['referido']
		print('referido: %s' %data)

		return data








# FORMULARIO DE LOGIN

class formlogin(forms.Form):
	username = forms.CharField(max_length=20,required=True,label="User",widget=(forms.EmailInput(attrs={'id':'email'})))
	password = forms.CharField(max_length=20,required=True,label="Password",widget=(forms.PasswordInput(attrs={'id':'password'})))



