from django.test import TestCase

# Create your tests here.

class homeView(TemplateView):
    template_name = "base/home.html"
    page_name = "home"

    def paginate_highlights(self, context):
        productos_qs = Producto.objects.filter(activo=True)
        user = self.request.session.get("username", None)
        prefer = False
        if user:
            prefer = True
        my_model = productos_qs.filter(destacado=True, by_producto_prefer=prefer)
        number_of_item = 6
        paginator = Paginator(my_model, number_of_item)
        first_page = paginator.page(1).object_list
        page_range = paginator.page_range
        context.update(
            {
                "paginator": paginator,
                "first_page": first_page,
                "page_range": page_range,
                "marcas": get_marcas(),
                "background": get_backgrounds(
                    filter={"codigo": self.request.resolver_match.url_name}
                ),
            }
        )
        if self.request.method == "POST":
            page_n = self.request.POST.get("page_n", None)
            results = list(paginator.page(page_n).object_list)
            return JsonResponse({"results": results})
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos_qs = get_productos()
        print(productos_qs)  # Imprimir productos en la consola
        user = self.request.session.get("username", None)
        prefer = False
        if user:
            prefer = True
        productos_hg = get_productos(
            **{"filter": {"destacado": True, "by_producto_prefer": prefer}}
        )
        categorias_qs = CategoriaProducto.objects.all()

        # Obtener la instancia de Pagina
        pagina_home = get_object_or_404(Pagina, pagename='Home')
        
        context.update(
            {
                "page_name": self.page_name,
                "productos": productos_qs,
                "productos_destacados": productos_hg,
                "marcas": get_marcas(),
                "categorias": categorias_qs,
                "background": get_backgrounds(
                    filter={"codigo": self.request.resolver_match.url_name}
                ),

                # Agregar los datos de la clase Pagina
                "pageslogan": pagina_home.pageslogan,
                "pagetitle": pagina_home.pagetitle,
                "pagename": pagina_home.pagename,
                "pagebanner": pagina_home.pagebanner,
                "pagebannermov": pagina_home.pagebannermov,
                "pagemetatitle": pagina_home.pagemetatitle,
                "pageogdesc": pagina_home.pageogdesc,
                "pagekeywords": pagina_home.pagekeywords,
                "pagemetadesc": pagina_home.pagemetadesc,
                "pageogurl": pagina_home.pageogurl,
                "pageogimg": pagina_home.pageogimg,
                "pageogurlsec": pagina_home.pageogurlsec,

                # Agregar la variable 'derechos_text' al contexto
                "derechos_text": "Texto de derechos que deseas mostrar",
            }
        )

        # Agregar la variable 'logged_user' al contexto
        logged_user = self.request.user  # Puedes usar self.request para obtener el usuario actual
        context["logged_user"] = logged_user

        return context

