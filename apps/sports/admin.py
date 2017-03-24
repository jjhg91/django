from django.contrib import admin

from apps.sports.models import deportes,ligas,equipos

# Register your models here.

class deportesAdmin(admin.ModelAdmin):
	list_display = ('deportes','foto_d')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class ligasAdmin(admin.ModelAdmin):
	list_display = ('id_ligas','ligas','id_deportes1','foto_l')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class equiposAdmin(admin.ModelAdmin):
	list_display = ('id_equipos','equipos','foto_e')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)



admin.site.register(deportes, deportesAdmin)
admin.site.register(ligas, ligasAdmin)
admin.site.register(equipos, equiposAdmin)

