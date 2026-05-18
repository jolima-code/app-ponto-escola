from django.urls import path
from .views import cadastro_funcionario


urlpatterns = [

    path(
        "cadastro/",
        cadastro_funcionario,
        name="cadastro_funcionario"
    ),

]