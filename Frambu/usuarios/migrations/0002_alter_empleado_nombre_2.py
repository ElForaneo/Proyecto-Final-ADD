# Generated by Django 4.0.4 on 2022-05-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='nombre_2',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
