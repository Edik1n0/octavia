# Generated by Django 4.2.5 on 2023-09-27 14:46

from django.db import migrations, models
import octavia.apps.inventario.models


class Migration(migrations.Migration):

    dependencies = [
        ("inventario", "0002_alter_categoriaproducto_imagen_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto",
            name="imagen",
            field=models.ImageField(
                blank=True,
                default="",
                null=True,
                storage=octavia.apps.inventario.models.S3ProductImage(),
                upload_to="teacompano-img/",
                verbose_name="Foto",
            ),
        ),
    ]