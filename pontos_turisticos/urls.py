from xml.dom.minidom import Document

from atracoes.api.viewsets import AtracaoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from core.api.viewsets import PontoTuristicoViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from enderecos.api.viewsets import EnderecoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename ='PontoTuristico') #identifica a rota e envia o viewset
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
