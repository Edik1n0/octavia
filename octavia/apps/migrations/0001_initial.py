# Generated by Django 4.2.5 on 2023-09-19 22:31

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Background",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo",
                    models.CharField(
                        choices=[
                            ("None", "Ninguno"),
                            ("tienda", "Tienda"),
                            ("nosotros", "Nosotros"),
                            ("home", "Home"),
                            ("contacto", "Contacto"),
                            ("videos", "Videos"),
                            ("politicas", "Politicas"),
                            ("videos", "Videos"),
                        ],
                        default="None",
                        max_length=45,
                        unique=True,
                        verbose_name="Codigo",
                    ),
                ),
                (
                    "video",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Video"
                    ),
                ),
                (
                    "titulo",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=100,
                        null=True,
                        verbose_name="Título",
                    ),
                ),
                (
                    "subtitulo",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=100,
                        null=True,
                        verbose_name="Subtítulo",
                    ),
                ),
                (
                    "enlace",
                    models.URLField(
                        blank=True, default="", null=True, verbose_name="Enlace"
                    ),
                ),
                (
                    "imagen",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="uploads/farsali/backgrounds/",
                        verbose_name="Imagen",
                    ),
                ),
                (
                    "activo",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="Activo"
                    ),
                ),
                ("orden", models.PositiveIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "Imagen Principal",
                "verbose_name_plural": "Imágenes Principales",
                "ordering": ("orden",),
            },
        ),
        migrations.CreateModel(
            name="Constante",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        choices=[
                            ("None", "Ninguno"),
                            ("contacto_email", "Email"),
                            ("contacto_telefono1", "Teléfono"),
                            ("contacto_telefono2", "Télefono 2"),
                            ("contacto_direccion", "Dirección"),
                            ("email_notificacion", "Email Notificacion"),
                            ("monto_min", "Monto Mínimo de Compra"),
                        ],
                        default="None",
                        max_length=45,
                        unique=True,
                        verbose_name="Codigo",
                    ),
                ),
                (
                    "enlace_texto",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="En caso de ser una constante que requiera un valor y un enlace externo",
                        max_length=200,
                        null=True,
                        verbose_name="Enlace",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("str", "Cadena"),
                            ("int", "Entero"),
                            ("list", "Lista"),
                            ("dict", "Diccionario"),
                            ("bool", "Boleano"),
                            ("datetime", "Fecha/Hora"),
                        ],
                        default="str",
                        max_length=10,
                        verbose_name="Tipo",
                    ),
                ),
                ("valor", models.TextField(verbose_name="Valor")),
                (
                    "icono_svg",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="uploads/farsali/constantes/",
                        verbose_name="Ícono SVG",
                    ),
                ),
                (
                    "icono",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="uploads/farsali/constantes/",
                        verbose_name="Ícono",
                    ),
                ),
            ],
            options={
                "verbose_name": "Constante",
                "verbose_name_plural": "Constantes",
            },
        ),
        migrations.CreateModel(
            name="Contacto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("telefono", models.CharField(max_length=50, verbose_name="Teléfono")),
                (
                    "contenido",
                    models.TextField(blank=True, null=True, verbose_name="Contenido"),
                ),
                ("orden", models.PositiveIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "Contacto",
                "verbose_name_plural": "Contactos",
                "ordering": ("orden",),
            },
        ),
        migrations.CreateModel(
            name="Generic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.CharField(max_length=100, verbose_name="Código")),
                ("titulo", models.CharField(max_length=75, verbose_name="Título")),
                (
                    "enlace",
                    models.URLField(
                        blank=True, default="", null=True, verbose_name="Enlace"
                    ),
                ),
                (
                    "imagen",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="uploads/farsali/imagenes/",
                        verbose_name="Imagen",
                    ),
                ),
                (
                    "subtitulo",
                    models.CharField(max_length=100, verbose_name="Subtítulo"),
                ),
                (
                    "descripcion",
                    models.TextField(blank=True, null=True, verbose_name="Descripcion"),
                ),
                (
                    "activo",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="Activo"
                    ),
                ),
                ("orden", models.PositiveIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "Generic",
                "verbose_name_plural": "Generics",
            },
        ),
        migrations.CreateModel(
            name="Imagen",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "enlace",
                    models.URLField(
                        blank=True, default="", null=True, verbose_name="Enlace"
                    ),
                ),
                ("codigo", models.CharField(max_length=100, verbose_name="Código")),
                ("titulo", models.CharField(max_length=75, verbose_name="Título")),
                (
                    "imagen",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="uploads/farsali/imagenes/",
                        verbose_name="Imagen",
                    ),
                ),
                (
                    "subtitulo",
                    models.CharField(max_length=100, verbose_name="Subtítulo"),
                ),
                (
                    "descripcion",
                    models.TextField(blank=True, null=True, verbose_name="Descripcion"),
                ),
                (
                    "activo",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="Activo"
                    ),
                ),
                ("orden", models.PositiveIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "Imagen",
                "verbose_name_plural": "Imagenes",
                "ordering": ("orden",),
            },
        ),
        migrations.CreateModel(
            name="Pagina",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pagename",
                    models.CharField(
                        max_length=200, verbose_name="Nombre de la página"
                    ),
                ),
                (
                    "pagemetatitle",
                    models.CharField(
                        max_length=200, verbose_name="Metatítulo(title) de la página"
                    ),
                ),
                (
                    "pagetitle",
                    models.CharField(
                        max_length=200, verbose_name="Título(h1) de la página"
                    ),
                ),
                (
                    "pageslogan",
                    models.CharField(
                        max_length=200, verbose_name="Slogan(h2) de la página"
                    ),
                ),
                (
                    "pagemetadesc",
                    ckeditor.fields.RichTextField(
                        verbose_name="Meta descripción de la página"
                    ),
                ),
                (
                    "pagekeywords",
                    ckeditor.fields.RichTextField(
                        verbose_name="Palabras clave de la página"
                    ),
                ),
                (
                    "pagebanner",
                    models.ImageField(
                        default="/servicios/static/img/default.jpg",
                        upload_to="teacompano-img/",
                        verbose_name="Imagen Banner de la página",
                    ),
                ),
                (
                    "pagebannermov",
                    models.ImageField(
                        default="/servicios/static/img/default-mov.jpg",
                        upload_to="teacompano-img/",
                        verbose_name="Imagen Banner de la página en Móvil",
                    ),
                ),
                (
                    "pageogdesc",
                    models.CharField(
                        default="Descripción del sitio web",
                        max_length=400,
                        verbose_name="Descripción OG de la página",
                    ),
                ),
                (
                    "pageogurl",
                    models.CharField(
                        max_length=200, verbose_name="Url OG de la página"
                    ),
                ),
                (
                    "pageogimg",
                    models.CharField(
                        max_length=200, verbose_name="Url OG Microformato de la página"
                    ),
                ),
                (
                    "pageogurlsec",
                    models.CharField(
                        max_length=200, verbose_name="Url OG Segura de la página"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pasarelas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=30, verbose_name="Nombre")),
                (
                    "origen",
                    models.SmallIntegerField(
                        choices=[(0, "MercadoPago"), (1, "Wompi"), (2, "Epayco")],
                        default=0,
                        unique=True,
                        verbose_name="Origen",
                    ),
                ),
                ("activo", models.BooleanField(default=False, verbose_name="Activo")),
            ],
            options={
                "verbose_name": "Pasarela",
                "verbose_name_plural": "Pasarelas",
            },
        ),
        migrations.CreateModel(
            name="RedSocial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ["TW", "Twitter"],
                            ["FB", "Facebook"],
                            ["11870", "11870"],
                            ["YTB", "Youtube"],
                            ["GP", "Google+"],
                            ["WP", "Wordpress"],
                            ["FR", "Flickr"],
                            ["PT", "Pinterest"],
                            ["FS", "Foursquare"],
                            ["TA", "Tripadvisor"],
                            ["LI", "LinkedIn"],
                            ["IN", "Instagram"],
                            ["VINE", "Vine"],
                            ["TUM", "Tumblr"],
                            ["VIM", "Vimeo"],
                            ["BL", "Blog"],
                        ],
                        default="TW",
                        max_length=10,
                        verbose_name="Tipo",
                    ),
                ),
                ("url", models.URLField(verbose_name="URL")),
                (
                    "icono_svg",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="uploads/farsali/red_social/",
                        verbose_name="Ícono SVG",
                    ),
                ),
                (
                    "icono",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="uploads/farsali/red_social/",
                        verbose_name="Ícono",
                    ),
                ),
                (
                    "codigo",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=20,
                        null=True,
                        verbose_name="Código",
                    ),
                ),
                ("orden", models.PositiveIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "Red social",
                "verbose_name_plural": "Redes sociales",
                "ordering": ("orden", "pk"),
            },
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=30, verbose_name="Título")),
                ("codigo", models.CharField(max_length=15, verbose_name="Codigo")),
                (
                    "imagen",
                    models.ImageField(
                        upload_to="uploads/videos/", verbose_name="Imagen"
                    ),
                ),
                (
                    "origen",
                    models.SmallIntegerField(
                        choices=[(0, "Youtube"), (1, "Vimeo")],
                        default=0,
                        verbose_name="Origen",
                    ),
                ),
                ("activo", models.BooleanField(default=True, verbose_name="Activo")),
                ("orden", models.PositiveIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "Video",
                "verbose_name_plural": "Videos",
                "ordering": ("orden",),
            },
        ),
        migrations.CreateModel(
            name="GaleriaGeneric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        blank=True, default="", max_length=100, verbose_name="Nombre"
                    ),
                ),
                (
                    "imagen",
                    models.ImageField(
                        max_length=200,
                        upload_to="uploads/cms_apps/imagenes/",
                        verbose_name="Imagen",
                    ),
                ),
                ("orden", models.PositiveIntegerField(default=0, verbose_name="Orden")),
                ("activo", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "generic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="genericgaleria_set",
                        to="apps.generic",
                        verbose_name="Noticia",
                    ),
                ),
            ],
            options={
                "verbose_name": "Galeria generics",
                "verbose_name_plural": "Galería de Generics",
                "ordering": ("orden",),
            },
        ),
    ]
