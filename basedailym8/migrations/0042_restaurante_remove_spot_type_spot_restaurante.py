# Generated by Django 4.1.1 on 2022-11-03 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0041_spot_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(blank=True, default='logo.png', null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('releasedate', models.DateTimeField()),
                ('restaurante', models.CharField(choices=[('Restaurante', 'spot_restaurante'), ('Bar', 'spot_bar'), ('Cafe', 'spot_cafe'), ('Discoteca', 'spot_disco'), ('Bar de Praia', 'spot_bardepraia')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='spot',
            name='type',
        ),
        migrations.AddField(
            model_name='spot',
            name='restaurante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.restaurante'),
        ),
    ]
