# coding: utf-8
from django.urls import path
from django.views.generic.base import TemplateView

from ..views import (
    ClienteViewMixin,
    ComentarioViewMixin,
    ContactoViewMixin,
    RecoveryPasswordViewMixin,
    activate_octavia,
    login_octavia,
    logout_octavia,
)
from .views import callbackGatewayMercadoPagoView  # ajax_highligths
from .views import (
    callbackGatewayWompiView,
    categoryView,
    checkoutView,
    contactoView,
    homeView,
    marcasView,
    nosotrosView,
    paymentCashView,
    paymentClienteView,
    paymentView,
    politicasView,
    productsDetailView,
    productsView,
    redesView,
    redirectPaymentView,
    registeroctavia,
    tiendaView,
    videosView,
)

urlpatterns = [
    path("", homeView.as_view(), name="home"),
    path("contacto/", ContactoViewMixin.as_view(), name="contacto"),
    path("videos/", videosView.as_view(), name="videos"),
    path("nosotros/", nosotrosView.as_view(), name="nosotros"),
    path("redes/", redesView.as_view(), name="redes"),
    path("politicas/", politicasView.as_view(), name="politicas"),
    path('tienda/<slug:producturl>/', ComentarioViewMixin.as_view(), name="productsDetailView"),
    path("marcas/<pk>/", marcasView.as_view(), name="marcas"),
    path("tienda/", tiendaView.as_view(), name="tienda"),
    path("compra/", checkoutView, name="checkout"),
    path("datos_cliente/", paymentClienteView, name="datos_cliente"),
    path("resumen_pago/", paymentView.as_view(), name="resumen_pago"),
    path("lista_productos/", productsView, name="lista_productos"),
    path("lista_categorias/", categoryView, name="lista_categorias"),
    # callback de las pasarelas de pagos
    path("callback_pago_wompi/", callbackGatewayWompiView, name="callback_pago_wompi"),
    path(
        "callback_pago_mercadopago/",
        callbackGatewayMercadoPagoView,
        name="callback_pago_mercadopago",
    ),
    path("redirect_pago/<reference>/", redirectPaymentView.as_view(), name="redirect_pago"),
    path("payment_cash/", paymentCashView, name="payment_cash"),
    path("registro_octavia/", ClienteViewMixin.as_view(), name="registro_octavia"),
    path("recuperar_contrasena/", RecoveryPasswordViewMixin.as_view(), name="recuperar_contrasena"),
    path(
        "activate_octavia/(?P<unicknameb64>[0-9A-Za-z_\-]+)/",
        activate_octavia,
        name="activate_octavia",
    ),
    path("login/", login_octavia, name="login_octavia"),
    path("logout/", logout_octavia, name="logout_octavia")
    # path('pagination/', ajax_highligths, name='ajax_highligths'),
]
