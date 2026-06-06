from django.db import models

class Equipamento(models.Model):
    nome_epi = models.CharField(max_length=100)
    ca = models.CharField(max_length=30)
    quantidade = models.PositiveIntegerField(default=0)
    validade = models.DateField()
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome_epi