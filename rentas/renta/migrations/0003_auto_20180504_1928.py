# Generated by Django 2.0.4 on 2018-05-04 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('renta', '0002_auto_20180504_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalles_renta',
            old_name='renta_id',
            new_name='renta',
        ),
    ]