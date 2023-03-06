from django.db import models

# Create your models here.
from django.db.models import CharField


class Usuario(models.Model):
    nome = models.CharField(max_length=60, null=False)
    email = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=14, null=False)
    tipo_user = models.CharField(max_length=4, null=True)

    def __str__(self) -> str:
        return self.nome


class Produto(models.Model):
    cod_produto = models.CharField(max_length=20, null=True)
    descricao = models.CharField(max_length=60, null=True)




class Preco_Produto(models.Model):
    valor = models.FloatField()
    data_valor = models.DateTimeField(auto_now=True)
    cod_valor = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)

