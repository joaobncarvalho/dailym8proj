# Generated by Django 4.1.1 on 2022-11-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0054_alter_estacionamento_lugares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='type',
            field=models.CharField(choices=[('Internacional', 'rest_internacional'), ('Americano', 'rest_americano'), ('Português', 'rest_portugues'), ('Chinês', 'rest_chines'), ('Italiano', 'rest_italiano'), ('Japonês', 'rest_japones')], max_length=20, null=True),
        ),
    ]
