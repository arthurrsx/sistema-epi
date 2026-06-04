from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.listar_emprestimos,
        name='listar_emprestimos'
    ),

    path(
        'cadastrar/',
        views.cadastrar_emprestimo,
        name='cadastrar_emprestimo'
    ),

    path(
        'editar/<int:id>/',
        views.editar_emprestimo,
        name='editar_emprestimo'
    ),

    path(
        'excluir/<int:id>/',
        views.excluir_emprestimo,
        name='excluir_emprestimo'
    ),

    path(
        'relatorios/',
        views.relatorios,
        name='relatorios'
    ),
]