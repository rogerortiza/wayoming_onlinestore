# Generated by Django 2.0.6 on 2019-02-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_detalleproducto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproducto',
            name='genero',
            field=models.CharField(blank=True, choices=[('H', 'Hombre'), ('M', 'Mujer'), ('N', 'Niño'), ('U', 'Unisex')], max_length=100),
        ),
    ]
