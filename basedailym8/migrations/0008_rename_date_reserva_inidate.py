# Generated by Django 4.1.1 on 2022-10-14 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0007_estabelecimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='date',
            new_name='inidate',
        ),
    ]
