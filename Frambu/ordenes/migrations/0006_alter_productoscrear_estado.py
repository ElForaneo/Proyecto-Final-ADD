# Generated by Django 4.0.4 on 2022-05-16 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0005_alter_productoscrear_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoscrear',
            name='estado',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='ordenes.estatus'),
        ),
    ]
