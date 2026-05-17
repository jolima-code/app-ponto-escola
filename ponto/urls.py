from django.urls import path

from .views import (
    bater_ponto,
    relatorio_ponto,
    exportar_excel,
    painel_coordenacao,
    exportar_coordenacao_excel,
    resumo_mensal,
    meu_banco_horas,
    exportar_banco_horas_excel,
    solicitar_compensacao,
    compensacoes_coordenacao,
    aprovar_compensacao,
    rejeitar_compensacao,
    documentos_coordenacao,
    aprovar_documento,
    rejeitar_documento,
    exportar_documentos_excel,
)

urlpatterns = [

    path(
        "",
        bater_ponto,
        name="bater_ponto"
    ),

    path(
        "relatorio/",
        relatorio_ponto,
        name="relatorio_ponto"
    ),

    path(
        "relatorio/excel/",
        exportar_excel,
        name="exportar_excel"
    ),

    path(
        "coordenacao/",
        painel_coordenacao,
        name="painel_coordenacao"
    ),

    path(
        "coordenacao/excel/",
        exportar_coordenacao_excel,
        name="exportar_coordenacao_excel"
    ),

    path(
        "resumo-mensal/",
        resumo_mensal,
        name="resumo_mensal"
    ),

    path(
        "banco-horas/",
        meu_banco_horas,
        name="meu_banco_horas"
    ),

    path(
        "banco-horas/excel/",
        exportar_banco_horas_excel,
        name="exportar_banco_horas_excel"
    ),

    path(
        "banco-horas/solicitar/",
        solicitar_compensacao,
        name="solicitar_compensacao"
    ),

    path(
        "coordenacao/compensacoes/",
        compensacoes_coordenacao,
        name="compensacoes_coordenacao"
    ),

    path(
        "coordenacao/compensacoes/<int:compensacao_id>/aprovar/",
        aprovar_compensacao,
        name="aprovar_compensacao"
    ),

    path(
        "coordenacao/compensacoes/<int:compensacao_id>/rejeitar/",
        rejeitar_compensacao,
        name="rejeitar_compensacao"
    ),

    path(
        "coordenacao/documentos/",
        documentos_coordenacao,
        name="documentos_coordenacao"
    ),

    path(
        "coordenacao/documentos/<int:documento_id>/aprovar/",
        aprovar_documento,
        name="aprovar_documento"
    ),

    path(
        "coordenacao/documentos/<int:documento_id>/rejeitar/",
        rejeitar_documento,
        name="rejeitar_documento"
    ),

    path(
        "coordenacao/documentos/excel/",
        exportar_documentos_excel,
        name="exportar_documentos_excel"
    ),

]