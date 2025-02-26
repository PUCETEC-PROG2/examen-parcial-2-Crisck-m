# Generated by Django 4.2 on 2025-01-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título de la película')),
                ('genre', models.CharField(max_length=100, verbose_name='Género de la película')),
                ('director', models.CharField(max_length=255, verbose_name='Nombre del director')),
                ('release_year', models.IntegerField(verbose_name='Año de publicación')),
                ('synopsis', models.TextField(verbose_name='Sinopsis')),
            ],
        ),
    ]
