# Generated by Django 5.1.6 on 2025-02-18 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AtractivosTuristicos', '0010_auto_20250218_1329'),
    ]

    operations = [
            migrations.RenameField(
            model_name='mirador',
            old_name='cerro',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='mirador',
            old_name='lugar',
            new_name='place',
        ),
        migrations.RenameField(
            model_name='mirador',
            old_name='calle',
            new_name='direccion',
        ),
    ]
