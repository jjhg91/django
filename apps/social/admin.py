from django.contrib import admin
from apps.social.models import statusSeguidor, seguidores, referidos, subReferidos 

# Register your models here.

class statusSeguidorAdmin(admin.ModelAdmin):
	list_display = ('id_statusSeguidor','statusSeguidor')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class seguidoresAdmin(admin.ModelAdmin):
	list_display = ('id_seguidor','id_seguido','id_statusSeguidor1')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class referidosAdmin(admin.ModelAdmin):
	list_display = ('id_usuarios3','id_referidos')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class subReferidosAdmin(admin.ModelAdmin):
	list_display = ('id_usuarios9','id_subReferidos')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

admin.site.register(statusSeguidor, statusSeguidorAdmin)
admin.site.register(seguidores, seguidoresAdmin)
admin.site.register(referidos, referidosAdmin)
admin.site.register(subReferidos, subReferidosAdmin)
