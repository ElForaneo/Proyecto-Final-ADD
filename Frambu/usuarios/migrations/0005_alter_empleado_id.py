# Generated by Django 4.0.4 on 2022-05-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_empleado_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
