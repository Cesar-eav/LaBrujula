# Generated by Django 5.1.6 on 2025-02-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtractivosTuristicos', '0012_auto_20250219_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streetart',
            name='direccion',
            field=models.TextField(verbose_name='direccion'),
        ),
    ]
