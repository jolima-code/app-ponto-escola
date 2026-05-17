from django.test import TestCase
from django.contrib.auth.models import User

from funcionarios.models import Funcionario
from ponto.models import RegistroPonto


class PontoTests(TestCase):

    def setUp(self):

        self.usuario = User.objects.create_user(
            username="maria",
            password="123456"
        )

        self.funcionario = Funcionario.objects.create(
            usuario=self.usuario,
            nome="Maria Teste",
            cpf="00000000000",
            cargo="Professora",
            setor="Maternal",
            data_admissao="2026-01-01",
            carga_horaria_diaria=8.00,
            ativo=True
        )

    def test_login_obrigatorio(self):

        resposta = self.client.get("/")

        self.assertEqual(
            resposta.status_code,
            302
        )

    def test_usuario_logado(self):

        self.client.login(
            username="maria",
            password="123456"
        )

        resposta = self.client.get("/")

        self.assertEqual(
            resposta.status_code,
            200
        )

    def test_registro_de_ponto(self):

        self.client.login(
            username="maria",
            password="123456"
        )

        self.client.post("/", {
            "tipo": "entrada",
            "observacao": "Teste"
        })

        self.assertEqual(
            RegistroPonto.objects.count(),
            1
        )