from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AtractivoTuristico(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    address = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    imagen = models.ImageField(upload_to='atractivos', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    atractivo_turistico = models.ForeignKey(AtractivoTuristico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

class StreetArt(models.Model):
    publicidad = models.BooleanField(verbose_name="Publicidad", default=False) 
    place = models.CharField(max_length=100, verbose_name="Lugar") 
    artista = models.CharField(max_length=100, verbose_name="Artista")  
    gps = models.CharField(max_length=100, verbose_name="GPS", default="Sin GPS") 
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Lat", default=0) 
    lon = models.DecimalField(max_digits=11, decimal_places=8, verbose_name="Lon", default=0)
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="articles", blank=True, null=True, verbose_name="Miniatura")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Street Art"
        verbose_name_plural = "Streets Arts"
        ordering = ['-created_at']
        db_table = 'AtractivosTuristicos_article'  # o cualquier otro nombre que desees


    def __str__(self):
        return f"{self.content} - {self.artista}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


### MIRADORES ###

class Mirador(models.Model):
    cerro = models.CharField(max_length=100, verbose_name="nombre", default="Cerro")
    lugar = models.CharField(max_length=100, verbose_name="Lugar", default="Nombre") 
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Lat", default=0) 
    lon = models.DecimalField(max_digits=11, decimal_places=8, verbose_name="Long", default=0)
    calle = models.CharField(max_length=100, verbose_name="calle", default="calle")   
    image = models.ImageField(upload_to="miradores", blank=True, null=True, verbose_name="Miniatura")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mirador"
        verbose_name_plural = "Miradores"
        db_table = "AtractivosTuristicos_mirador"


    def __str__(self):
        return f"{self.lugar}"


### OTROS ###

class Otro(models.Model):
    lugar = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Lat", default=0) 
    lon = models.DecimalField(max_digits=11, decimal_places=8, verbose_name="Lon", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="otros", blank=True, null=True, verbose_name="Miniatura")

    class Meta:
        verbose_name = "Otro"
        verbose_name_plural = "Otros"

    def __str__(self):
        return f"{self.lugar} - {self.descripcion}"


### IGLESIAS ###

class Iglesia(models.Model):
    nombre = models.CharField(max_length=100, default="")
    direccion = models.CharField(max_length=100, default="")
    lugar = models.CharField(max_length=100, default="")
    descripcion = models.TextField(max_length=250)
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Lat", default=0) 
    lon = models.DecimalField(max_digits=11, decimal_places=8, verbose_name="Lon", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="iglesias", blank=True, null=True, verbose_name="Miniatura")

    class Meta:
        verbose_name = "Iglesia"
        verbose_name_plural = "Iglesias"
        ordering = ['-created_at']
        db_table = 'AtractivosTuristicos_iglesia'  # o cualquier otro nombre que desees


    def __str__(self):
        return f"{self.nombre}"


class Ascensor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Lat", default=0) 
    lon = models.DecimalField(max_digits=11, decimal_places=8, verbose_name="Lon", default=0)
    content = models.TextField(verbose_name="Descripción", default="Describir")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="ascensores", blank=True, null=True, verbose_name="Miniatura")

    class Meta:
        verbose_name = "Ascensor"
        db_table = "AtractivosTuristicos_ascensor"


# ---------------------------------
class Escalera(models.Model):
    modelos = models.CharField(max_length=100, default="")
    lugar = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    autor = models.CharField(max_length=100, default="")
    direccion = models.CharField(max_length=250, default="dir")
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Lat", default=0)
    lon = models.DecimalField(max_digits=11, decimal_places=8, verbose_name="Lon", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="escaleras", blank=True, null=True, verbose_name="Miniatura")

    class Meta:
        verbose_name = "Escalera"
        verbose_name_plural = "Escaleras"
        db_table = "AtractivosTuristicos_escalera"


    def __str__(self):
        return f"{self.descripcion}"


class Arquitectura(models.Model):
    publicidad = models.BooleanField(verbose_name="Publicidad", default=False)
    lugar = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250, default="dir")
    antecedentes = models.TextField(max_length=250, default="")
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Lat", default=0)
    lon = models.DecimalField(max_digits=11, decimal_places=8, verbose_name="Lon", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="arquitectura", blank=True, null=True, verbose_name="Miniatura")

    class Meta:
        verbose_name = "Arquitectura"
        verbose_name_plural = "Arquitecturas"
        db_table = "AtractivosTuristicos_arquitectura"


    def __str__(self):
        return f"{self.descripcion}"


class Publicidad(models.Model):
    publicidad = models.BooleanField(default=False)
    local_nombre = models.CharField(max_length=100, verbose_name="Local")
    direccion = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Lat", default=0)
    lon = models.DecimalField(max_digits=11, decimal_places=8, verbose_name="Lon", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="publicidad", blank=True, null=True, verbose_name="Miniatura")

    class Meta:
        verbose_name = "Publicidad"
        verbose_name_plural = "Publicidades"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.local_nombre}"


