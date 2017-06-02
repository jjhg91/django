import django
from apps.sports.models import deportes
from apps.users.models import puntos

from django.contrib.auth.decorators import login_required


def list_deportes(request):
	deporte = deportes.objects.all()
	return deporte

@login_required()
def list_puntos(request):
	usuario = request.user.id
	punto = puntos.objects.filter(id_usuarios2__id=usuario).values('acumulados','enJuego')
	return punto

@login_required()
def user_image(request):
	usuario = request.user
	foto = "/media/%s"%usuario.usuarios.foto
	return foto


def my_processor(request):

	context = {'lista_deportes':list_deportes(request),'pts':list_puntos(request),'user_foto':user_image(request),}
	return context
