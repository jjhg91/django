from django import forms

from apps.users.models import usuarios



 #FORMULARIO 1
'''
class formlogin(forms.ModelForm):
	class Meta: 
		
		model = usuarios

		fields = [
			'correo',
			'contra',
		]
		labels = {
			'correo' : 'Email',
			'contra' : 'Password',
		}

		widgets = {
			'correo' : forms.EmailInput(attrs={'placeholder':'dime tu correo','class':'win','id':'puente'}),
			'contra' : forms.PasswordInput(attrs={'placeholder':'dime tu clave'}),
		}


'''
#FORMULARIO 2 

class formlogin(forms.Form):
	username = forms.CharField(max_length=10,required=True,label="Email",widget=(forms.TextInput(attrs={'placeholder':'escribe tu correo','id':'email'})))
	password = forms.CharField(max_length=10,required=True,label="Password",widget=(forms.TextInput(attrs={'placeholder':'escribe tu clave','id':'password'})))
