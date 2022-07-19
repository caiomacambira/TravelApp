from django.db import models
from django.forms import CharField
from pyexpat import model


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.nome
