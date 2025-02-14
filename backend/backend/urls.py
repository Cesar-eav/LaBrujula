
from django.contrib import admin
from django.urls import path, include
# from AtractivosTuristicos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atractivos/', include('AtractivosTuristicos.urls')),
    path('', include('AtractivosTuristicos.urls')),  # Agrega esta línea

]
