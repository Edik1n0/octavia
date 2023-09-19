from django.contrib import admin

from django.utils.translation import gettext_lazy as _
from .models import Cliente
from rangefilter.filters import (
    DateRangeFilter
)

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'cedula',
        'email',
        'is_octavia',
        'created',
        'fecha_activacion',
    )
    list_display_links = (
        'id',
    )
    list_filter = (
        'is_octavia',
        ('fecha_activacion', DateRangeFilter),  # Usar DateRangeFilter en lugar de DateRangeFilterBuilder
        ('created', DateRangeFilter),         # Usar DateTimeRangeFilter en lugar de DateRangeFilterBuilder
    )
    search_fields = [
        'nombre',
        'email',
    ]

    fieldsets = [
        [_(u'General'), {
            'fields': (
                'nombre',
                'cedula',
                'nick_name',
                'contrasena',
                'email',
                'is_octavia',
                'locacion',
                'telefono',
                'direccion'
            )
        }]
    ]

admin.site.register(Cliente, ClienteAdmin)
