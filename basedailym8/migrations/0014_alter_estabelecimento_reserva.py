# Generated by Django 4.1.1 on 2022-10-14 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0013_rename_date_estabelecimento_releasedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='reserva',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.reserva'),
        ),
    ]
