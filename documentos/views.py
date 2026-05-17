from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from funcionarios.models import Funcionario
from .models import Documento


@login_required
def enviar_documento(request):

    funcionario = Funcionario.objects.get(
        usuario=request.user
    )

    documentos = Documento.objects.filter(
        funcionario=funcionario
    ).order_by("-data_envio")

    if request.method == "POST":

        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        arquivo = request.FILES.get("arquivo")

        Documento.objects.create(
            funcionario=funcionario,
            titulo=titulo,
            descricao=descricao,
            arquivo=arquivo
        )

        return redirect("enviar_documento")

    return render(request, "documentos/enviar_documento.html", {
        "documentos": documentos,
    })