from django.shortcuts import get_object_or_404, render, redirect
from .models import Pagina, Promo, Generic, Product, Carrito
from django.views.generic import DetailView
from .forms import CarritoForm
from django.contrib import messages

# Create your views here.

def index(request):
    # video =get_object_or_404(Video, videoname='Sheer Elegance')
    pagina_home = get_object_or_404(Pagina, pagename='Home')
    promos = Promo.objects.all()
    
    # Filtra los productos destacados
    destacados = Product.objects.filter(destacado=True)

    generic = Generic.objects.all()
    pageslogan = pagina_home.pageslogan
    pagetitle = pagina_home.pagetitle
    pagename = pagina_home.pagename
    pagebanner = pagina_home.pagebanner
    pagebannermov = pagina_home.pagebannermov
    pagemetatitle = pagina_home.pagemetatitle
    pageogdesc = pagina_home.pageogdesc
    pagekeywords = pagina_home.pagekeywords
    pagemetadesc = pagina_home.pagemetadesc
    pageogurl = pagina_home.pageogurl
    pageogimg = pagina_home.pageogimg
    pageogurlsec = pagina_home.pageogurlsec
    videourl = pagina_home.videourl
    
    context = {
        'generic': generic,
        'pageslogan': pageslogan,
        'pagetitle': pagetitle,
        'pagename': pagename,
        'pagebanner': pagebanner,
        'pagebannermov': pagebannermov,
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'videourl': videourl,
        'promos': promos,
        'destacados': destacados,  # Agrega la lista de productos destacados al contexto
    }
    
    return render(request, 'home.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'producto-detalle.html'
    context_object_name = 'producto'

    def get_object(self):
        return get_object_or_404(Product, producturl=self.kwargs['producturl'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.object.productogtitle
        context['keywords'] = self.object.productkeywords
        context['mdescription'] = self.object.productmetadesc
        context['ogurl'] = self.object.productogurl
        context['ogimg'] = self.object.productogimg
        context['ogtitle'] = self.object.productogtitle
        context['ogurlimg'] = self.object.productogurlsec
        context['ogdesc'] = self.object.productogdesc

        # Agregar la lista de promociones al contexto
        promos = Promo.objects.all()
        context['promos'] = promos

        return context

def tienda(request):
    # Resto de tu código para obtener datos de página
    pagina_tienda = get_object_or_404(Pagina, pagename='Tienda')
    promos = Promo.objects.all()
    pageslogan = pagina_tienda.pageslogan
    pagetitle = pagina_tienda.pagetitle
    pagename = pagina_tienda.pagename
    pagebanner = pagina_tienda.pagebanner
    pagebannermov = pagina_tienda.pagebannermov
    pagemetatitle = pagina_tienda.pagemetatitle
    pageogdesc = pagina_tienda.pageogdesc
    pagekeywords = pagina_tienda.pagekeywords
    pagemetadesc = pagina_tienda.pagemetadesc
    pageogurl = pagina_tienda.pageogurl
    pageogimg = pagina_tienda.pageogimg
    pageogurlsec = pagina_tienda.pageogurlsec

    # Obtener los productos en la tienda
    productos = Product.objects.all()

    # Obtener el carrito del usuario actual
    carrito, creado = Carrito.objects.get_or_create(user=request.user)
    form = CarritoForm()  # Crea una instancia del formulario

    if request.method == 'POST':
        # Si la solicitud es un POST, procesa el formulario y añade el producto al carrito
        form = CarritoForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            producto = get_object_or_404(Product, id=product_id)
            carrito.products.add(producto)

    # Obtener los productos en el carrito del usuario actual
    productos_en_carrito = carrito.products.all()

    return render(request, 'tienda.html', {
        'productos': productos,  # Asegúrate de que esta variable esté presente en el contexto
        'productos_en_carrito': productos_en_carrito,  # Agrega esta variable al contexto
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan,
        'promos': promos,
    })

def carrito(request):
    if request.method == 'POST':
        producto_id = request.POST['producto_id']
        cantidad = int(request.POST['cantidad'])

        try:
            producto = Product.objects.get(id=producto_id)
        except Product.DoesNotExist:
            messages.error(request, 'El producto no existe')
            return redirect('detalle_producto', producto_id=producto_id)

        # Lógica para agregar el producto al carrito
        # Por ejemplo, puedes crear una instancia de CarritoItem y guardarla en la base de datos

        messages.success(request, 'Producto agregado al carrito')
        return redirect('detalle_producto', producto_id=producto_id)
