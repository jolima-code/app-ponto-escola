from django.db import models
from funcionarios.models import Funcionario


class SaldoBancoHoras(models.Model):

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE
    )

    data = models.DateField()

    horas_trabalhadas = models.DurationField()

    horas_previstas = models.DurationField()

    saldo = models.DurationField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.funcionario.nome} - {self.data}"
    
class FechamentoBancoHoras(models.Model):

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE
    )

    mes = models.IntegerField()

    ano = models.IntegerField()

    saldo_final = models.DurationField()

    fechado_em = models.DateTimeField(
        auto_now_add=True
    )

    fechado = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.funcionario.nome} - {self.mes}/{self.ano}"
    
class CompensacaoBancoHoras(models.Model):

    TIPO_CHOICES = [
        ("credito", "Crédito"),
        ("debito", "Débito"),
    ]

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE
    )

    data = models.DateField()

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    quantidade = models.DurationField()

    motivo = models.TextField()

    aprovado = models.BooleanField(
        default=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.funcionario.nome} - {self.tipo} - {self.data}"