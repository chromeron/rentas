# Generated by Django 2.0.4 on 2018-05-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostosCanchaParticular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(max_length=100)),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CostosEscuelaExterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(max_length=100)),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CostosLigas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(choices=[('A', 'Zona A'), ('B', 'Zona B')], max_length=1)),
                ('tipo', models.CharField(choices=[('SPNyS', 'Soccer pasto natural y sintético'), ('PS7', 'Pasto sintético 7'), ('PS6yR', 'Pasto sintético 6 y rápido'), ('CFRy6', 'Cemento fútbol rápido y 6'), ('ST', 'Soccer Tierra'), ('Multiusos', 'Multiusos')], max_length=30)),
                ('categoria', models.CharField(choices=[('Libre', 'Libre'), ('J y F', 'Juvenil y Femenil'), ('Infantil', 'Infantil')], max_length=20)),
                ('costo', models.IntegerField()),
            ],
        ),
    ]
