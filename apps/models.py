from django.db import models
from ckeditor.fields import RichTextField
from storages.backends.s3boto3 import S3Boto3Storage
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Asesor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Generic(models.Model):
    gentitle = models.CharField(max_length=400, blank=True)
    genimg = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen para el generic", default='apps/static/img/default-c.jpg', blank=True)
    gendesc = RichTextField(verbose_name="Descripción del Contenido genérico")
    genasesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True)
    gencreated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gentitle
    
class S3ProductImage(S3Boto3Storage):
    location = 'teacompano-img'
    file_overwrite = False

class Galeria(models.Model):
    identificador = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='teacompano-img/')  # 'galeria/' es el directorio en S3 donde se guardarán las imágenes

    def __str__(self):
        return self.identificador
    
class Pagina(models.Model):
    pagename = models.CharField(max_length=200, verbose_name="Nombre de la página")
    pagemetatitle = models.CharField(max_length=200, verbose_name="Metatítulo(title) de la página")
    pagetitle = models.CharField(max_length=200, verbose_name="Título(h1) de la página")
    pageslogan = models.CharField(max_length=200, verbose_name="Slogan(h2) de la página")
    pagemetadesc = RichTextField(verbose_name="Meta descripción de la página")
    pagekeywords = RichTextField(verbose_name="Palabras clave de la página")
    pagebanner = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner de la página", default='apps/static/img/default.jpg')
    pagebannermov = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner de la página en Móvil", default='apps/static/img/default-c.jpg')
    pageogdesc = models.CharField(max_length=400, verbose_name="Descripción OG de la página", default='Descripción del sitio web')
    pageogurl = models.CharField(max_length=200, verbose_name="Url OG de la página")
    pageogimg = models.CharField(max_length=200, verbose_name="Url OG Microformato de la página")
    pageogurlsec = models.CharField(max_length=200, verbose_name="Url OG Segura de la página")
    videourl = models.CharField(max_length=200, verbose_name="Video de la página", default='GduZ3mELr_E?si=xSvEBdzOXiQJN4gs')

    def __str__(self):
        return self.pagename
    
class Product(models.Model):
    # Elementos del header del producto
    productmetadesc = models.CharField(max_length=200, verbose_name="Meta descripción del Producto")
    productkeywords = RichTextField(verbose_name="Palabras clave del Producto")
    productbanner = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen Banner del Producto", default='/productos/static/img/default.jpg')
    productbannermov = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen Banner del Producto en Móvil", default='/productos/static/img/default-mov.jpg')
    # Elementos OG del producto
    productogdesc = models.CharField(max_length=200, verbose_name="Descripción OG del Producto")
    productogtitle =models.CharField(max_length=200, verbose_name="Metatítulo OG del Producto")
    productogurl = models.CharField(max_length=200, verbose_name="Url OG del Producto")
    productogimg = models.CharField(max_length=200, verbose_name="Url OG Microformato del Producto")
    productogurlsec = models.CharField(max_length=200, verbose_name="Url OG Segura del Producto")
    # Elementos Visuales del producto
    productref = models.CharField(max_length=200, verbose_name="Referencia del Producto", default=0)
    productname = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    productslogan = models.CharField(max_length=200, verbose_name="Slogan del Producto")
    productoldprice = models.IntegerField(verbose_name="Precio normal", blank=True, default=0, null=True)
    productdiscount = models.IntegerField(verbose_name="Valor de descuento", blank=True, default=0, null=True)
    producturl = models.CharField(max_length=200, verbose_name="Url producto detalle")
    productdescription = RichTextField()
    productimg = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen principal del Producto")
    destacado = models.BooleanField(default=False, verbose_name="Producto destacado")
    gallerya = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen secundaria del Producto", blank=True)
    galleryb = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen adicional del Producto", blank=True)
    galleryc = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen final del Producto", blank=True)
    # productimg = models.ImageField(upload_to='static/img/uploads/', verbose_name="Imagen principal del Producto")
    asesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True)
    productprice = models.IntegerField(verbose_name="Precio de venta", blank=True, null=True, editable=False)
    productupdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productname + ' - creado por - ' + self.asesor.name

    def save(self, *args, **kwargs):
        self.productupdated = timezone.now()
        if self.productoldprice is not None and self.productdiscount is not None:
            self.productprice = self.productoldprice - (self.productoldprice * self.productdiscount / 100)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

class Video(models.Model):
    videoname = models.CharField(max_length=200, verbose_name="Nombre del video")
    videourl = models.CharField(max_length=200, verbose_name="URL del video")

    def __str__(self):
        return self.videoname
    
class Promo(models.Model):
    promoname = models.CharField(max_length=200, verbose_name="Nombre de la promoción")
    widepromo = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen wide promo", default='/productos/static/img/default-mov.jpg')
    movilpromo = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen movil promo", default='/productos/static/img/default-mov.jpg')

    def __str__(self):
        return self.promoname
    
class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', blank=True)

    def __str__(self):
        return f'Carrito de {self.user.username}'