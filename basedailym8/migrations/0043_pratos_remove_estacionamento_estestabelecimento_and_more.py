# Generated by Django 4.1.1 on 2022-11-03 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0042_restaurante_remove_spot_type_spot_restaurante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(blank=True, default='logo.png', null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='estacionamento',
            name='EstEstabelecimento',
        ),
        migrations.RemoveField(
            model_name='restaurante',
            name='restaurante',
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='featured_image',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='releasedate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='type',
            field=models.CharField(choices=[('Internacional', 'rest_internacional'), ('Americano', 'rest_americano'), ('Português', 'rest_portugues'), ('Chinês', 'rest_chines'), ('Italiano', 'rest_italiano')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='spot',
            name='estacionamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.estacionamento'),
        ),
        migrations.AlterField(
            model_name='estacionamento',
            name='lugares',
            field=models.IntegerField(null=False,default='120'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='releasedate',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='Praiaequip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(blank=True, default='logo.png', null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('releasedate', models.DateTimeField(null=True)),
                ('lugares', models.IntegerField(default='')),
                ('type', models.CharField(choices=[('Espreguiçadeira', 'equi_espreguicadeira'), ('Toldo', 'equi_toldo')], max_length=20)),
                ('restaurante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(blank=True, default='logo.png', null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('pratos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.pratos')),
            ],
        ),
        migrations.AddField(
            model_name='restaurante',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.menu'),
        ),
        migrations.AddField(
            model_name='spot',
            name='praiaequip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.praiaequip'),
        ),
    ]
