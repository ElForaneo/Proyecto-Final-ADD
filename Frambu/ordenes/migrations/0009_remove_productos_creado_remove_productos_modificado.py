# Generated by Django 4.0.4 on 2022-05-16 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0008_productos_creado_productos_modificado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='creado',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='modificado',
        ),
    ]
