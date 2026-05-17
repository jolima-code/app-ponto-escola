from django.contrib import admin
from .models import Documento


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):

    list_display = (
        "funcionario",
        "titulo",
        "status",
        "data_envio",
        "arquivo",
    )

    list_filter = (
        "status",
        "data_envio",
        "funcionario",
    )

    search_fields = (
        "funcionario__nome",
        "titulo",
        "descricao",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "data_envio",
    )