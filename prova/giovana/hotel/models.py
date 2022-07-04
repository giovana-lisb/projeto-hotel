from mailbox import NotEmptyError
from django.db import models

# Create your models here.
class Cidade (models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return self.nome


class Hospede (models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(max_length=20)
    email = models.EmailField()
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

class Produto (models.Model):
    nome = models.CharField(max_length=100)
    valor = models.IntegerField(max_length=100)
    
    def __str__(self):
        return self.nome

class TidoEstadia (models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome


class Estadia (models.Model):
    valor = models.IntegerField(max_length=100)
    data = models.DateField()
    observacao = models.CharField(max_length=500)
    Hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    TidoEstadia = models.ForeignKey(TidoEstadia, on_delete=models.CASCADE)
    Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


    

