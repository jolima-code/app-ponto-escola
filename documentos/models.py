from django.db import models
from funcionarios.models import Funcionario


class Documento(models.Model):

    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),
        ("rejeitado", "Rejeitado"),
    ]

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE
    )

    titulo = models.CharField(max_length=200)

    descricao = models.TextField(
        blank=True,
        null=True
    )

    arquivo = models.FileField(
        upload_to="documentos/"
    )

    data_envio = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pendente"
    )

    def __str__(self):
        return f"{self.funcionario.nome} - {self.titulo}"