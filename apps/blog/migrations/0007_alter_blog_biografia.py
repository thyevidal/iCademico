# Generated by Django 3.2 on 2021-04-15 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_biografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='biografia',
            field=models.CharField(max_length=200, null=True, verbose_name='Biografia'),
        ),
    ]
