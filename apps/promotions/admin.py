from django.contrib import admin
from apps.promotions.models import bonusDiario, promociones, promoRealizada

# Register your models here.

class bonusDiarioAdmin(admin.ModelAdmin):
	list_display = ('id_bonusDiario','seguidilla','puntos')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class promocionesAdmin(admin.ModelAdmin):
	list_display = ('id_promocion','promocion','tipoPromocion', 'puntosObtener', 'fotoPromocion')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

class promoRealizadaAdmin(admin.ModelAdmin):
	list_display = ('id_usuarios6','id_promocion1')
#	list_filter = ('')
#	search_fields = ('')
#	filter_horizontal = ('',)

admin.site.register(bonusDiario, bonusDiarioAdmin)
admin.site.register(promociones, promocionesAdmin)
admin.site.register(promoRealizada, promoRealizadaAdmin)
