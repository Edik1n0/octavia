from django.contrib import admin
from .models import Asesor, Product, Pagina, Video, Promo, Galeria, Generic

# Register your models here.
class GaleriaAdmin(admin.ModelAdmin):
    list_display = (
        'identificador',
    )

admin.site.register(Galeria, GaleriaAdmin)

admin.site.register(Asesor)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'productref',
        'productname',
        'asesor',
        'productupdated',
    )

    actions = ['copy_product']

    def copy_product(self, request, queryset):
        for product in queryset:
            product.pk = None  # Asignar None al campo PK para que se cree una copia
            product.productname += ' (Copia)'  # Cambiar el nombre para indicar que es una copia
            product.save()

    copy_product.short_description = "Duplicar productos seleccionados"

admin.site.register(Product, ProductAdmin)

class GenericAdmin(admin.ModelAdmin):
    list_display = (
        'gentitle',
        'genasesor',
        'gencreated'
    )

admin.site.register(Generic, GenericAdmin)
admin.site.register(Pagina)
admin.site.register(Video)
admin.site.register(Promo)