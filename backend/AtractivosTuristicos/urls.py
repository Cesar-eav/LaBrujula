from django.urls import path, include
from rest_framework import routers
from AtractivosTuristicos import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

# Primer parametro es la parte final de la url
router.register(r'AtractivosTuristicos', views.AtractivoTuristicoView, 'atractivos')
router.register(r'ascensores', views.AscensorView, 'ascensores')
router.register(r'murales', views.StreetArtView, 'murales')
router.register(r'iglesias', views.IglesiaView, 'iglesias')
router.register(r'escaleras', views.EscaleraView, 'escaleras')
router.register(r'arquitectura', views.ArquitecturaView, 'arquitectura')
router.register(r'miradores', views.MiradorView, 'miradores')



urlpatterns = [
    path("api/v1/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
