from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Emprestimo
from .forms import EmprestimoForm


def listar_emprestimos(request):

    emprestimos = Emprestimo.objects.all()

    return render(
        request,
        'emprestimos/listar.html',
        {'emprestimos': emprestimos}
    )


def cadastrar_emprestimo(request):

    form = EmprestimoForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Empréstimo cadastrado com sucesso!'
        )

        return redirect('listar_emprestimos')

    return render(
        request,
        'emprestimos/cadastrar.html',
        {'form': form}
    )


def editar_emprestimo(request, id):

    emprestimo = get_object_or_404(
        Emprestimo,
        id=id
    )

    form = EmprestimoForm(
        request.POST or None,
        instance=emprestimo
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Empréstimo atualizado com sucesso!'
        )

        return redirect('listar_emprestimos')

    return render(
        request,
        'emprestimos/editar.html',
        {'form': form}
    )


def excluir_emprestimo(request, id):

    emprestimo = get_object_or_404(
        Emprestimo,
        id=id
    )

    emprestimo.delete()

    messages.success(
        request,
        'Empréstimo excluído com sucesso!'
    )

    return redirect('listar_emprestimos')


def relatorios(request):

    emprestimos = Emprestimo.objects.all()

    colaborador = request.GET.get('colaborador', '')
    equipamento = request.GET.get('equipamento', '')
    status = request.GET.get('status', '')

    if colaborador:
        emprestimos = emprestimos.filter(
            colaborador__nome__icontains=colaborador
        )

    if equipamento:
        emprestimos = emprestimos.filter(
            equipamento__nome_epi__icontains=equipamento
        )

    if status:
        emprestimos = emprestimos.filter(
            status=status
        )

    return render(
        request,
        'emprestimos/relatorios.html',
        {
            'emprestimos': emprestimos,
            'colaborador': colaborador,
            'equipamento': equipamento,
            'status': status,
        }
    )