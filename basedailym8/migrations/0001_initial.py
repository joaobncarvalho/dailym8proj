# Generated by Django 4.1.2 on 2022-10-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('UserEmail', models.CharField(max_length=200)),
                ('UserMatricula', models.CharField(max_length=8)),
                ('UserPassword', models.CharField(max_length=25)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
