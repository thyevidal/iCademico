# Generated by Django 3.2 on 2021-04-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_biografia'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobre',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
