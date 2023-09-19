from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .views import ProductDetailView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('tienda/', views.tienda, name="tienda"),
    path('carrito/', views.carrito, name="carrito"),
    path('tienda/<slug:producturl>/', ProductDetailView.as_view(), name='product_detail'),
    path('nosotros/', views.index, name="nosotros"),
    path('servicios/', views.index, name="servicios"),
    path('contacto/', views.index, name="contacto"),
    path('pauta/', views.index, name="pauta"),
    path('cookies/', views.index, name="cookies"),
    path('privacidad/', views.index, name="privacy"),
]