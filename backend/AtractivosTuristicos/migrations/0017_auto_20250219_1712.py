# Generated by Django 5.1.6 on 2025-02-19 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AtractivosTuristicos', '0016_remove_arquitectura_contenido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name = 'escalera',
            old_name = 'lugar',
            new_name = 'place',
        ),
        migrations.RenameField(
            model_name = 'escalera',
            old_name = 'descripcion',
            new_name = 'nombre',
        ),
        
    ]
