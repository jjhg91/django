from django.contrib import admin

from apps.plays.models import resultadoJugadas,jugadas,pote,jugadaPote,porra,porraEquipos,jugadaPorra,partidos

# Register your models here.

class resultadoJugadasAdmin(admin.ModelAdmin):
	list_display = ('id_rjugada','resultadoJ')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class jugadasAdmin(admin.ModelAdmin):
	list_display = ('id_jugadas','id_usuarios1','id_partidos1','puntosJugados',
					'puntosGanar','jugada','fechaJugada','id_rjugada1')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class poteAdmin(admin.ModelAdmin):
	list_display = ('id_pote','id_partidos2','costePote','premioPote')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class jugadaPoteAdmin(admin.ModelAdmin):
	list_display = ('id_usuarios10','id_pote1','resultadoHPote','resultadoVPote',
					'fechaPote','id_resultadoPote1')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class porraAdmin(admin.ModelAdmin):
	list_display = ('id_porra','nombrePorra','premioPorra')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class porraEquiposAdmin(admin.ModelAdmin):
	list_display = ('id_porra4','id_partidos4','id_rjugada')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class jugadaPorraAdmin(admin.ModelAdmin):
	list_display = ('id_usuarios11','id_porra2','id_partidos5','id_jugadaPorra')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class partidosAdmin(admin.ModelAdmin):
	list_display = ('id_partidos','id_equiposh','id_equiposv',
					'id_ligas2','fecha','home','empate','visitante','puntuacion_h',
					'puntuacion_v','actualizado')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)


admin.site.register(resultadoJugadas, resultadoJugadasAdmin)
admin.site.register(jugadas, jugadasAdmin)
admin.site.register(pote, poteAdmin)
admin.site.register(jugadaPote, jugadaPoteAdmin)
admin.site.register(porra, porraAdmin)
admin.site.register(porraEquipos, porraEquiposAdmin)
admin.site.register(jugadaPorra, jugadaPorraAdmin)
admin.site.register(partidos, partidosAdmin)
