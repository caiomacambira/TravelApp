from avaliacoes.models import Avaliacao
from rest_framework.viewsets import ModelViewSet

from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
