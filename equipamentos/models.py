from django.db import models

class Equipamento(models.Model):
    nome_epi = models.CharField(max_length=100)
    ca = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    validade = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome_epi