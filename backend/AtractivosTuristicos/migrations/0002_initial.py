# Generated by Django 5.1.5 on 2025-02-08 15:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AtractivosTuristicos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquitectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicidad', models.BooleanField(default=False, verbose_name='Publicidad')),
                ('lugar', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('direccion', models.CharField(default='dir', max_length=250)),
                ('antecedentes', models.TextField(default='', max_length=250)),
                ('lat', models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Lat')),
                ('lon', models.DecimalField(decimal_places=8, default=0, max_digits=11, verbose_name='Lon')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='arquitectura', verbose_name='Miniatura')),
            ],
            options={
                'verbose_name': 'Arquitectura',
                'verbose_name_plural': 'Arquitecturas',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicidad', models.BooleanField(default=False, verbose_name='Publicidad')),
                ('title', models.CharField(max_length=100, verbose_name='Lugar')),
                ('artista', models.CharField(max_length=100, verbose_name='Artista')),
                ('lat', models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Lat')),
                ('lon', models.DecimalField(decimal_places=8, default=0, max_digits=11, verbose_name='Lon')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Miniatura')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Street Art',
                'verbose_name_plural': 'Streets Arts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Ascensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=250)),
                ('lat', models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Lat')),
                ('lon', models.DecimalField(decimal_places=8, default=0, max_digits=11, verbose_name='Lon')),
                ('content', models.TextField(default='Describir', verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ascensores', verbose_name='Miniatura')),
            ],
            options={
                'verbose_name': 'Ascensor',
            },
        ),
        migrations.CreateModel(
            name='AtractivoTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('latitud', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitud', models.DecimalField(decimal_places=8, max_digits=11)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='atractivos')),
                ('is_verified', models.BooleanField(default=False)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Escalera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelos', models.CharField(default='', max_length=100)),
                ('lugar', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('autor', models.CharField(default='', max_length=100)),
                ('direccion', models.CharField(default='dir', max_length=250)),
                ('lat', models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Lat')),
                ('lon', models.DecimalField(decimal_places=8, default=0, max_digits=11, verbose_name='Lon')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='escaleras', verbose_name='Miniatura')),
            ],
            options={
                'verbose_name': 'Escalera',
                'verbose_name_plural': 'Escaleras',
            },
        ),
        migrations.CreateModel(
            name='Iglesia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('direccion', models.CharField(default='', max_length=100)),
                ('lugar', models.CharField(default='', max_length=100)),
                ('descripcion', models.TextField(max_length=250)),
                ('lat', models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Lat')),
                ('lon', models.DecimalField(decimal_places=8, default=0, max_digits=11, verbose_name='Lon')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='iglesias', verbose_name='Miniatura')),
            ],
            options={
                'verbose_name': 'Iglesia',
                'verbose_name_plural': 'Iglesias',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Mirador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cerro', models.CharField(default='Cerro', max_length=100, verbose_name='nombre')),
                ('lugar', models.CharField(default='Nombre', max_length=100, verbose_name='Lugar')),
                ('lat', models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Lat')),
                ('lon', models.DecimalField(decimal_places=8, default=0, max_digits=11, verbose_name='Long')),
                ('calle', models.CharField(default='calle', max_length=100, verbose_name='calle')),
                ('image', models.ImageField(blank=True, null=True, upload_to='miradores', verbose_name='Miniatura')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mirador',
                'verbose_name_plural': 'Miradores',
            },
        ),
        migrations.CreateModel(
            name='Otro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('lat', models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Lat')),
                ('lon', models.DecimalField(decimal_places=8, default=0, max_digits=11, verbose_name='Lon')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='otros', verbose_name='Miniatura')),
            ],
            options={
                'verbose_name': 'Otro',
                'verbose_name_plural': 'Otros',
            },
        ),
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicidad', models.BooleanField(default=False)),
                ('local_nombre', models.CharField(max_length=100, verbose_name='Local')),
                ('direccion', models.CharField(max_length=100)),
                ('lugar', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=250)),
                ('lat', models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Lat')),
                ('lon', models.DecimalField(decimal_places=8, default=0, max_digits=11, verbose_name='Lon')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='publicidad', verbose_name='Miniatura')),
            ],
            options={
                'verbose_name': 'Publicidad',
                'verbose_name_plural': 'Publicidades',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('calificacion', models.IntegerField(default=0)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('atractivo_turistico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AtractivosTuristicos.atractivoturistico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
