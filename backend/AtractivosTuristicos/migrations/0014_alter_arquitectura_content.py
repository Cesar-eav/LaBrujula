# Generated by Django 5.1.6 on 2025-02-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtractivosTuristicos', '0013_alter_streetart_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquitectura',
            name='content',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
