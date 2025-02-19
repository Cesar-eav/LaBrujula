from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget 

from .models import Arquitectura, Ascensor, AtractivoTuristico, Iglesia, Escalera, Comentario, StreetArt, Mirador

# Register your models here.

admin.site.register(StreetArt)
admin.site.register(Arquitectura) 
admin.site.register(Ascensor)
admin.site.register(Iglesia)
admin.site.register(Escalera)
admin.site.register(Comentario)
admin.site.register(Mirador)