from core.models import PontoTuristico
from rest_framework.viewsets import ModelViewSet

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    queryset = PontoTuristico.objects.all() #pegando tudo do banco de dados
    serializer_class = PontoTuristicoSerializer
