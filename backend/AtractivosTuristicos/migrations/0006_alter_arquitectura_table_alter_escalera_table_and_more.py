# Generated by Django 5.1.5 on 2025-02-11 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AtractivosTuristicos', '0005_alter_iglesia_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='arquitectura',
            table='AtractivosTuristicos_arquitectura',
        ),
        migrations.AlterModelTable(
            name='escalera',
            table='AtractivosTuristicos_escalera',
        ),
        migrations.AlterModelTable(
            name='mirador',
            table='AtractivosTuristicos_mirador',
        ),
    ]
