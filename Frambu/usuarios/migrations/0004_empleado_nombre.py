# Generated by Django 4.0.4 on 2022-05-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_empleado_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]