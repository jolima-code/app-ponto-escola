from django.contrib import admin
from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "cargo", "setor", "data_admissao", "ativo")
    search_fields = ("nome", "cpf", "email")
    list_filter = ("ativo", "cargo", "setor")