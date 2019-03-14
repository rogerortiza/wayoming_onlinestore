# Generated by Django 2.0.6 on 2018-07-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20180706_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Accesorios', 'Accesorios'), ('Botas', 'Botas'), ('Chamarras', 'Chamarras'), ('Cintos', 'Cintos'), ('Sombreros', 'Sombreros'), ('Zapatos', 'Zapatos')], max_length=100),
        ),
    ]
