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
    
        
class Ascensor(AtractivoTuristico):
    año_construcción = models.IntegerField()
    altura = models.DecimalField(max_digits=10, decimal_places=2)
    is_monument = models.BooleanField(default=False)
    is_functional = models.BooleanField(null=True)
    
class Iglesia(AtractivoTuristico):
    año_construcción = models.IntegerField()
    denominacion =  models.CharField(max_length=50, blank=True)
    is_monument = models.BooleanField(default=False)

class Arquitectura(AtractivoTuristico):
    año_construcción = models.IntegerField()
    is_monument = models.BooleanField(default=False)
 
class Mural(AtractivoTuristico):
    artista = models.CharField(max_length=255)
    instagram =  models.CharField(max_length=50, blank=True)

class Escalera(AtractivoTuristico):
    longitud_escalera = models.DecimalField(max_digits=10, decimal_places=2)
    número_peldaños = models.IntegerField()
    
class Comentario(models.Model):
    atractivo_turistico = models.ForeignKey(AtractivoTuristico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)