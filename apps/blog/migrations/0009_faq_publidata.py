# Generated by Django 3.2 on 2021-04-15 23:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_sobre_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='publidata',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]