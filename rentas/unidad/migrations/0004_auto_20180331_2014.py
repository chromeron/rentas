# Generated by Django 2.0.3 on 2018-03-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidad', '0003_tipo_cancha_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_cancha',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
