# Generated by Django 4.0.4 on 2022-05-16 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0009_remove_productos_creado_remove_productos_modificado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={'ordering': ['id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]