# Generated by Django 4.1.1 on 2022-10-14 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basedailym8', '0012_alter_reserva_fimdate_alter_reserva_inidate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estabelecimento',
            old_name='date',
            new_name='releasedate',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
