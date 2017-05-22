import django
from apps.sports.models import deportes
from apps.users.models import puntos


def list_deportes(request):
	deporte = deportes.objects.all()
	return deporte

def list_puntos(request):
	usuario = request.user
	punto = puntos.objects.filter(id_usuarios2__id_usuarios=usuario).values('acumulados','enJuego')
	return punto

def user_image(request):
	usuario = request.user
	foto = "/media/%s"%usuario.usuarios.foto
	return foto


def my_processor(request):

	context = {'lista_deportes':list_deportes(request),'pts':list_puntos(request),'user_foto':user_image(request),}
	return context
