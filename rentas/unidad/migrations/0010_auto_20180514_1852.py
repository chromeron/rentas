# Generated by Django 2.0.4 on 2018-05-14 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unidad', '0009_auto_20180514_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo_cancha',
            old_name='liga_infantil',
            new_name='costo_liga_infantil',
        ),
    ]
