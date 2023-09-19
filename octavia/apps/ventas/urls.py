from django.urls import path
from octavia.apps.ventas import views

app_name = "resumen_ventas"

urlpatterns = [
    path("control/resumen_ventas/", views.ResumenVentasView.as_view(), name="resumen_ventas"),
]
