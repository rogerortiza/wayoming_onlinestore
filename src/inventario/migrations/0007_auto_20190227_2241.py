# Generated by Django 2.0.6 on 2019-02-27 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_auto_20180706_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.CategoriasProductos'),
        ),
    ]
