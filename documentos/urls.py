from django.urls import path
from .views import enviar_documento


urlpatterns = [
    path(
        "",
        enviar_documento,
        name="enviar_documento"
    ),
]