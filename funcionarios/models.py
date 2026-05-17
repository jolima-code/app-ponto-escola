from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)

    cargo = models.CharField(max_length=100)

    setor = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    data_admissao = models.DateField()
    setor = models.CharField(max_length=100, blank=True, null=True)

    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    data_admissao = models.DateField()

    carga_horaria_diaria = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=8.00
    )
    
    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome