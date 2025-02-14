from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import ArticleSerializer, CategorySerializer, MiradorSerializer, OtroSerializer, IglesiaSerializer, AscensorSerializer, EscaleraSerializer, ArquitecturaSerializer, AtractivoTuristicoSerializer, ComentarioSerializer, PublicidadSerializer
from .models import Article, Category, Mirador, Otro, Iglesia, Ascensor, Escalera, Arquitectura, AtractivoTuristico, Comentario, Publicidad


# La vista ArticleView maneja las solicitudes HTTP utilizando los métodos list, create, retrieve, update y destroy. 
# Estos métodos se encargan de devolver respuestas adecuadas para cada tipo de solicitud.
# Create your views here.

class ArticleView(viewsets.ModelViewSet):
    
    serializer_class = ArticleSerializer
    
    #Devuelve todos los datos del modelo Article
    queryset = Article.objects.all()
    
    def list(self, request):
        try:
            return super().list(request)
        except TypeError as e:
            print(e)
            return Response({'error': str(e)})


class CategoryView(viewsets.ModelViewSet):
    
    serializer_class = CategorySerializer
    
    #Devuelve todos los datos del modelo Category
    queryset = Category.objects.all()


class MiradorView(viewsets.ModelViewSet):
    
    serializer_class = MiradorSerializer
    
    #Devuelve todos los datos del modelo Mirador
    queryset = Mirador.objects.all()


class OtroView(viewsets.ModelViewSet):
    
    serializer_class = OtroSerializer
    
    #Devuelve todos los datos del modelo Otro
    queryset = Otro.objects.all()


class IglesiaView(viewsets.ModelViewSet):
    
    serializer_class = IglesiaSerializer
    
    #Devuelve todos los datos del modelo Iglesia
    queryset = Iglesia.objects.all()


class AscensorView(viewsets.ModelViewSet):
    
    serializer_class = AscensorSerializer
    
    #Devuelve todos los datos del modelo Ascensor
    queryset = Ascensor.objects.all()


class EscaleraView(viewsets.ModelViewSet):
    
    serializer_class = EscaleraSerializer
    
    #Devuelve todos los datos del modelo Escalera
    queryset = Escalera.objects.all()


class ArquitecturaView(viewsets.ModelViewSet):
    
    serializer_class = ArquitecturaSerializer
    
    #Devuelve todos los datos del modelo Arquitectura
    queryset = Arquitectura.objects.all()


class AtractivoTuristicoView(viewsets.ModelViewSet):
    
    serializer_class = AtractivoTuristicoSerializer
    
    #Devuelve todos los datos del modelo AtractivoTuristico
    queryset = AtractivoTuristico.objects.all()


class ComentarioView(viewsets.ModelViewSet):
    
    serializer_class = ComentarioSerializer
    
    #Devuelve todos los datos del modelo Comentario
    queryset = Comentario.objects.all()


class PublicidadView(viewsets.ModelViewSet):
    
    serializer_class = PublicidadSerializer
    
    #Devuelve todos los datos del modelo Publicidad
    queryset = Publicidad.objects.all()