from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from octavia.apps import views

admin.site.index_title = "Welcome to Octavia Researcher Portal"
admin.empty_value_display = "**Empty**"

urlpatterns = [
    path("control/", admin.site.urls),
    path("", include("octavia.apps.navegacion.urls")),
    path("", include("octavia.apps.ventas.urls")),
]

handler404 = views.error_404

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
