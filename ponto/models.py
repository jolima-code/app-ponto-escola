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
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    data_hora = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.funcionario.nome} - {self.get_tipo_display()} - {self.data_hora}"