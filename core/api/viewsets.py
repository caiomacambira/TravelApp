from core.models import PontoTuristico
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    #queryset = PontoTuristico.objects.all() #pegando tudo do banco de dados
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self,request,*args,**kwargs): 
    #     return Response({'teste':123})

    # def create(self,request,*args,**kwargs):
    #     return Response({'Hello':request.data['nome']})
