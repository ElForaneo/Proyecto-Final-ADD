# Generated by Django 4.0.4 on 2022-05-16 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0010_alter_productos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={'ordering': ['-id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
