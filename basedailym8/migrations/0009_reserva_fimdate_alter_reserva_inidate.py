# Generated by Django 4.1.1 on 2022-10-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0008_rename_date_reserva_inidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fimdate',
            field=models.DateTimeField(default='2022-10-14'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='inidate',
            field=models.DateTimeField(default='2002-08-10'),
        ),
    ]
