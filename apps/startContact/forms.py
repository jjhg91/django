from django import forms
from django.contrib.auth.models import User
from apps.users.models import usuarios


 #FORMULARIO 1
'''
class formlogin(forms.ModelForm):
	class Meta: 
		
		model = User
		fields = ['username', 'password',]
		labels = {'username' : 'Usuario', 'password' : 'Clave',}
		widgets = {
			'username' : forms.TextInput(attrs={'placeholder':'dime tu correo','class':'win','id':'puente'}),
			'password' : forms.TextInput(attrs={'placeholder':'dime tu clave'}),
		}
'''


#FORMULARIO 2 

class formlogin(forms.Form):
	username = forms.CharField(max_length=20,required=True,label="User",widget=(forms.EmailInput(attrs={'id':'email'})))
	password = forms.CharField(max_length=20,required=True,label="Password",widget=(forms.PasswordInput(attrs={'id':'password'})))



