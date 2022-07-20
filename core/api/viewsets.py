from core.models import PontoTuristico
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    #queryset = PontoTuristico.objects.all() #pegando tudo do banco de dados
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao']

    def get_queryset(self):
        id = self.request.query_params.get('id',None)
        nome = self.request.query_params.get('nome',None)
        descricao =  self.request.query_params.get('descricao',None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self,request,*args,**kwargs): 
    #     return Response({'teste':123})

    # def create(self,request,*args,**kwargs):
    #     return Response({'Hello':request.data['nome']})
