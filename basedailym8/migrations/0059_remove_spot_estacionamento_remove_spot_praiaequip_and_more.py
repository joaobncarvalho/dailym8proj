# Generated by Django 4.1.1 on 2022-11-06 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0058_alter_reserva_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='estacionamento',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='praiaequip',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='restaurante',
        ),
        migrations.AddField(
            model_name='praiaequip',
            name='praia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.praia'),
        ),
    ]
