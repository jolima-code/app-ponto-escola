from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

from .models import Funcionario


def cadastro_funcionario(request):

    if request.method == "POST":

        nome = request.POST.get("nome")
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if senha != confirmar_senha:
            messages.error(
                request,
                "As senhas não conferem."
            )

            return redirect("cadastro_funcionario")

        if User.objects.filter(username=username).exists():
            messages.error(
                request,
                "Este usuário já existe."
            )

            return redirect("cadastro_funcionario")

        usuario = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        funcionario = Funcionario.objects.create(
            usuario=usuario,
            nome=nome,
            cpf="",
            cargo="A definir",
            setor="A definir",
            data_admissao="2026-01-01",
            carga_horaria_diaria=8.00,
            ativo=True
        )

        login(request, usuario)

        messages.success(
            request,
            "Cadastro realizado com sucesso!"
        )

        return redirect("bater_ponto")

    return render(
        request,
        "funcionarios/cadastro.html"
    )