# Generated by Django 4.1.1 on 2022-10-14 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0006_alter_reserva_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=20)),
                ('reserva', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='basedailym8.reserva')),
            ],
        ),
    ]
