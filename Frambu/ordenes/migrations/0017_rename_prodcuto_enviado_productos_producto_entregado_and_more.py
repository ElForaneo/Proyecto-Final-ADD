# Generated by Django 4.0.4 on 2022-05-16 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0016_alter_productos_producto_pedido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='prodcuto_enviado',
            new_name='producto_entregado',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='produto_entregado',
            new_name='producto_enviado',
        ),
    ]
