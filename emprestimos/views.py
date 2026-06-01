from django.shortcuts import render, redirect, get_object_or_404
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

    if request.method == 'POST':
        emprestimo.delete()
        return redirect('listar_emprestimos')

    return render(
        request,
        'emprestimos/excluir.html',
        {'emprestimo': emprestimo}
    )