from django.contrib import admin
from .models import Arquitectura, Ascensor, AtractivoTuristico, Iglesia, Escalera, Comentario, Article, Mirador

# Register your models here.

admin.site.register(Article)
admin.site.register(Arquitectura) 
admin.site.register(Ascensor)
admin.site.register(Iglesia)
admin.site.register(Escalera)
admin.site.register(Comentario)
admin.site.register(Mirador)