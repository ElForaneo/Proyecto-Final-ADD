# Generated by Django 4.0.4 on 2022-05-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0013_alter_productos_prodcuto_enviado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='prodcuto_enviado',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='producto_pedido',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
