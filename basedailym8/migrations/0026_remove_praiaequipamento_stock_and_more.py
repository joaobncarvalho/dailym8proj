# Generated by Django 4.1.1 on 2022-10-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0025_alter_praiaequipamento_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='praiaequipamento',
            name='stock',
        ),
        migrations.AddField(
            model_name='praiaequipamento',
            name='equipamentos',
            field=models.IntegerField(default=300),
        ),
    ]