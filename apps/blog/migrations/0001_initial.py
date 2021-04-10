# Generated by Django 3.2 on 2021-04-10 03:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('texte', models.TextField(verbose_name='Texto')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='blog/images', verbose_name='Imagem')),
                ('criacaodata', models.DateTimeField(default=django.utils.timezone.now)),
                ('publidata', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
