# Generated by Django 4.2.5 on 2023-09-27 23:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventario", "0006_rename_url_producto_producturl"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="productbanner",
            field=models.ImageField(
                default="/productos/static/img/default.jpg",
                upload_to="imagenes-decortinas/",
                verbose_name="Imagen Banner del Producto",
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="productbannermov",
            field=models.ImageField(
                default="/productos/static/img/default-mov.jpg",
                upload_to="imagenes-decortinas/",
                verbose_name="Imagen Banner del Producto en Móvil",
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="productkeywords",
            field=ckeditor.fields.RichTextField(
                default="", verbose_name="Palabras clave del Producto"
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="productmetadesc",
            field=models.CharField(
                default="", max_length=200, verbose_name="Meta descripción del Producto"
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="productogdesc",
            field=models.CharField(
                default="", max_length=200, verbose_name="Descripción OG del Producto"
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="productogimg",
            field=models.CharField(
                default="",
                max_length=200,
                verbose_name="Url OG Microformato del Producto",
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="productogtitle",
            field=models.CharField(
                default="", max_length=200, verbose_name="Metatítulo OG del Producto"
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="productogurl",
            field=models.CharField(
                default="", max_length=200, verbose_name="Url OG del Producto"
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="productogurlsec",
            field=models.CharField(
                default="", max_length=200, verbose_name="Url OG Segura del Producto"
            ),
        ),
    ]