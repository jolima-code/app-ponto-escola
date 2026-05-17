from django.contrib import admin
from .models import RegistroPonto


@admin.register(RegistroPonto)
class RegistroPontoAdmin(admin.ModelAdmin):

    list_display = (
        "funcionario",
        "tipo",
        "data_hora",
        "status_entrada",
    )

    search_fields = (
        "funcionario__nome",
        "funcionario__cpf",
    )

    list_filter = (
        "tipo",
        "data_hora",
    )

    def status_entrada(self, obj):

        if obj.data_hora.hour > 7:
            return "Atrasado"

        if obj.data_hora.hour == 7 and obj.data_hora.minute > 0:
            return "Atrasado"

        return "No horário"

    status_entrada.short_description = "Entrada"