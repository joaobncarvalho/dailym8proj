# Generated by Django 4.1.1 on 2022-10-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0039_alter_reserva_type_alter_spot_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='type',
            field=models.CharField(choices=[('Almoço', 'almoco'), ('Lanche', 'lanche'), ('Jantar', 'jantar'), ('Beber um Copo', 'copo')], max_length=20),
        ),
    ]
