# Generated by Django 4.1.1 on 2022-10-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0023_praiaequipamento_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praiaequipamento',
            name='stock',
            field=models.IntegerField(default='500'),
        ),
    ]
