# Generated by Django 4.0.2 on 2024-06-01 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='State'),
        ),
    ]
