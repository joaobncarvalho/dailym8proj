# Generated by Django 4.1.1 on 2022-11-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0040_alter_reserva_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='featured_image',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=''),
        ),
    ]
