from django.contrib import admin

from apps.users.models import pais,zonaHoraria,postal,nombre,apellido,natalidad,ediPerfil,nivelUsuario,genero,usuarios,statusUsario,puntos

# Register your models here.
#'usuario','correo','contra',
class usuariosAdmin(admin.ModelAdmin):
	list_display = ('id_nombre1','id_apellido1','foto','banner','id_zhoraria1')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class apellidoAdmin(admin.ModelAdmin):
	list_display = ('id_apellido','apellido')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class nivelUsuarioAdmin(admin.ModelAdmin):
	list_display = ('id_nivUsuario','nivelUsuario')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class statusUsuarioAdmin(admin.ModelAdmin):
	list_display = ('id_stusUsuario','stusUsuario')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class ediPerfilAdmin(admin.ModelAdmin):
	list_display = ('id_edPerfil','edPerfil')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class nombreAdmin(admin.ModelAdmin):
	list_display = ('id_nombre','nombre')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class natalidadAdmin(admin.ModelAdmin):
	list_display = ('id_natalidad','natalidad')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class generoAdmin(admin.ModelAdmin):
	list_display = ('id_genero','genero')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class zonaHorariaAdmin(admin.ModelAdmin):
	list_display = ('id_zhoraria','zhoraria')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class paisAdmin(admin.ModelAdmin):
	list_display = ('id_pais','pais')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class postalAdmin(admin.ModelAdmin):
	list_display = ('id_postal','postal')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class puntosAdmin(admin.ModelAdmin):
	list_display = ('id_usuarios2','jugadas','jugadasGanadas','potes','potesGanados','quinelas','quinelasGanadas',
					'bonusDiario','promociones','referidos','subReferidos','enJuego','regalos',
					'acumulados')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)


admin.site.register(usuarios, usuariosAdmin)
admin.site.register(nivelUsuario, nivelUsuarioAdmin)
admin.site.register(statusUsario, statusUsuarioAdmin)
admin.site.register(ediPerfil, ediPerfilAdmin)
admin.site.register(nombre, nombreAdmin)
admin.site.register(apellido, apellidoAdmin)
admin.site.register(natalidad, natalidadAdmin)
admin.site.register(genero, generoAdmin)
admin.site.register(zonaHoraria, zonaHorariaAdmin)
admin.site.register(pais, paisAdmin)
admin.site.register(postal, postalAdmin)
admin.site.register(puntos, puntosAdmin)








	