from django.db import models
from funcionarios.models import Funcionario


class RegistroPonto(models.Model):
    TIPO_CHOICES = [
        ("entrada", "Entrada"),
        ("saida_almoco", "Saída para almoço"),
        ("retorno_almoco", "Retorno do almoço"),
        ("saida", "Saída"),
    ]

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    data_hora = models.DateTimeField(auto_now_add=True)

    observacao = models.TextField(
        blank=True,
        null=True
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    distancia_metros = models.FloatField(
        blank=True,
        null=True
    )

    localizacao_valida = models.BooleanField(
        default=False
    )

    def __str__(self):
        return (
            f"{self.funcionario.nome} - "
            f"{self.get_tipo_display()} - "
            f"{self.data_hora}"
        )