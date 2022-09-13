from django.urls import path
from .views import UsuarioView, CaiView

urlpatterns = [
    path("usuarios/", UsuarioView.as_view(), name="usuarios_list"),
    path("usuarios/<int:id>", UsuarioView.as_view(), name="usuarios_process"),
    path("cais", CaiView.as_view(), name="Cai get"),
]
