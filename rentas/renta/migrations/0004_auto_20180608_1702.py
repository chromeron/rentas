# Generated by Django 2.0.5 on 2018-06-08 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renta', '0003_auto_20180504_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_elaboracion', models.DateField(default=None)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='renta',
            name='costo',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='renta',
            name='detalles',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='renta',
            name='especial',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='renta',
            name='status',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='renta',
            name='trimestre',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='renta',
            name='contrato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='renta.Contrato'),
        ),
    ]
