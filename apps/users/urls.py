"""finish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.users.views import jugada, perfil, editperfil, infpersonal, enjuego, referido, busqueda

from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^(?P<url_perfil>\d+)/$', login_required(perfil.as_view()), name='perfil'),
    url(r'^(?P<url_perfil>\d+)/edit/$', login_required(editperfil.as_view()), name='editperfil'),
    url(r'^(?P<url_perfil>\d+)/private/$', login_required(infpersonal.as_view()), name='infpersonal'),
	url(r'^(?P<url_perfil>\d+)/jugadas/(?P<url_jugadas>\w+)/$', login_required(jugada.as_view()), name='jugadas'),
	url(r'^(?P<url_perfil>\d+)/referidos/(?P<url_referido>["primarios","secundarios"]\w+)/$', login_required(referido.as_view()), name='referido'),
    url(r'^busqueda/$', busqueda.as_view(), name='busqueda'),
]
