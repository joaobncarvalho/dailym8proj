# Generated by Django 4.1.1 on 2022-11-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0048_alter_estacionamento_releasedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamento',
            name='releasedate',
            field=models.DateTimeField(blank=True, default='2022-03-11 16:00:00.000000'),
        ),
        migrations.AlterField(
            model_name='praiaequip',
            name='releasedate',
            field=models.DateTimeField(blank=True, default='2022-03-11 16:00:00.000000'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fimdate',
            field=models.DateTimeField(blank=True, default='2022-03-11 16:00:00.000000'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='inidate',
            field=models.DateTimeField(blank=True, default='2022-03-11 16:00:00.000000'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='releasedate',
            field=models.DateTimeField(blank=True, default='2022-03-11 16:00:00.000000'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='releasedate',
            field=models.DateTimeField(blank=True, default='2022-03-11 16:00:00.000000'),
        ),
    ]
