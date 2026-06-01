from django.db import models
from django.utils import timezone

from colaboradores.models import Colaborador
from equipamentos.models import Equipamento


class Emprestimo(models.Model):

    STATUS_CHOICES = [
        ('EMPRESTADO', 'Emprestado'),
        ('FORNECIDO', 'Fornecido'),
        ('DEVOLVIDO', 'Devolvido'),
        ('DANIFICADO', 'Danificado'),
        ('PERDIDO', 'Perdido'),
    ]

    colaborador = models.ForeignKey(
        Colaborador,
        on_delete=models.CASCADE
    )

    equipamento = models.ForeignKey(
        Equipamento,
        on_delete=models.CASCADE
    )

    data_emprestimo = models.DateTimeField(
        auto_now_add=True
    )

    data_prevista_devolucao = models.DateTimeField()

    data_devolucao = models.DateTimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='EMPRESTADO'
    )

    observacao_devolucao = models.TextField(
        null=True,
        blank=True
    )

    def clean(self):
        if self.data_prevista_devolucao and self.data_prevista_devolucao <= timezone.now():
            raise ValueError("Data prevista deve ser futura.")

    def __str__(self):
        return f"{self.colaborador} - {self.equipamento}"