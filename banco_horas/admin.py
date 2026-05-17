from django.contrib import admin
from .models import (
    SaldoBancoHoras,
    FechamentoBancoHoras,
    CompensacaoBancoHoras,
)


@admin.register(SaldoBancoHoras)
class SaldoBancoHorasAdmin(admin.ModelAdmin):

    list_display = (
        "funcionario",
        "data",
        "horas_trabalhadas",
        "horas_previstas",
        "saldo",
    )

    list_filter = (
        "data",
        "funcionario",
    )

    search_fields = (
        "funcionario__nome",
    )


@admin.register(FechamentoBancoHoras)
class FechamentoBancoHorasAdmin(admin.ModelAdmin):

    list_display = (
        "funcionario",
        "mes",
        "ano",
        "saldo_final",
        "fechado",
        "fechado_em",
    )

    list_filter = (
        "mes",
        "ano",
        "fechado",
    )

    search_fields = (
        "funcionario__nome",
    )


@admin.register(CompensacaoBancoHoras)
class CompensacaoBancoHorasAdmin(admin.ModelAdmin):

    list_display = (
        "funcionario",
        "data",
        "tipo",
        "quantidade",
        "aprovado",
    )

    list_filter = (
        "tipo",
        "aprovado",
        "data",
    )

    search_fields = (
        "funcionario__nome",
        "motivo",
    )

    list_editable = (
        "aprovado",
    )