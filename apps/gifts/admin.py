from django.contrib import admin
from apps.gifts.models import regalos, statusRegalo, regaloObtenido

# Register your models here.

class regalosAdmin(admin.ModelAdmin):
	list_display = ('id_regalos','regalo','puntosNecesarios','fotoRegalo','descripcionRegalo')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class statusRegaloAdmin(admin.ModelAdmin):
	list_display = ('id_statusRegalo','statusRegalo')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class regaloObtenidoAdmin(admin.ModelAdmin):
	list_display = ('id_usuarios5','id_regalos1','id_statusRegalo1')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

admin.site.register(regalos, regalosAdmin)
admin.site.register(statusRegalo, statusRegaloAdmin)
admin.site.register(regaloObtenido, regaloObtenidoAdmin)