from rest_framework import serializers
from .models import StreetArt, Category, Mirador, Otro, Iglesia, Ascensor, Escalera, Arquitectura, AtractivoTuristico, Comentario, Publicidad

class StreetArtSerializer(serializers.ModelSerializer):
    
    lat = serializers.DecimalField(max_digits=10, decimal_places=8)
    lon = serializers.DecimalField(max_digits=11, decimal_places=8)
    
    class Meta: 
        model = StreetArt
        fields = '__all__'
        
    def to_representation(self, instance):
        try:
            data = super().to_representation(instance)
            return data
        except TypeError as e:
            print(f"Error: {e}")
            print(f"Instance: {instance}")
            print(f"Fields: {self.fields}")
            raise

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = '__all__'

class MiradorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Mirador
        fields = '__all__'

class OtroSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Otro
        fields = '__all__'

class IglesiaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Iglesia
        fields = '__all__'

class AscensorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ascensor
        fields = '__all__'

class EscaleraSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Escalera
        fields = '__all__'

class ArquitecturaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Arquitectura
        fields = '__all__'

class AtractivoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtractivoTuristico
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'


class PublicidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicidad
        fields = '__all__'