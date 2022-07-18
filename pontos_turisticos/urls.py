from atracoes.api import viewsets
from atracoes.api.viewsets import AtracoesViewSet
from core.api.viewsets import PontoTuristicoViewSet
from django import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet) #identifica a rota e envia o viewset
router.register(r'atracoes', AtracoesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
