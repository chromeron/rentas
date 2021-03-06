# Generated by Django 2.0.4 on 2018-05-14 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0002_auto_20180514_1759'),
        ('unidad', '0007_auto_20180514_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_cancha',
            name='costo_escuela',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='costos.CostosEscuelaExterna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipo_cancha',
            name='costo_liga_jyf',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, related_name='juvenilyfemenil', to='costos.CostosLiga'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipo_cancha',
            name='costo_liga_libre',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, related_name='libre', to='costos.CostosLiga'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipo_cancha',
            name='costo_particular',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='costos.CostosCanchaParticular'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipo_cancha',
            name='liga_infantil',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, related_name='infantil', to='costos.CostosLiga'),
            preserve_default=False,
        ),
    ]
