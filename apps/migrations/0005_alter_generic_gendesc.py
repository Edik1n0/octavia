# Generated by Django 4.1.5 on 2023-09-18 21:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0004_generic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generic",
            name="gendesc",
            field=ckeditor.fields.RichTextField(
                verbose_name="Descripción del Contenido genérico"
            ),
        ),
    ]
