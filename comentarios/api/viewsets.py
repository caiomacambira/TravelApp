from comentarios.models import Comentario
from rest_framework.viewsets import ModelViewSet

from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
