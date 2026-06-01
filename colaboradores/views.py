from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaborador
from .forms import ColaboradorForm


def listar_colaboradores(request):

    busca = request.GET.get('buscar')

    if busca:
        colaboradores = Colaborador.objects.filter(nome__icontains=busca)
    else:
        colaboradores = Colaborador.objects.all()

    return render(request, 'colaboradores/listar.html', {
        'colaboradores': colaboradores
    })


def cadastrar_colaborador(request):

    form = ColaboradorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_colaboradores')

    return render(request, 'colaboradores/cadastrar.html', {
        'form': form
    })


def editar_colaborador(request, id):

    colaborador = get_object_or_404(Colaborador, id=id)

    form = ColaboradorForm(
        request.POST or None,
        instance=colaborador
    )

    if form.is_valid():
        form.save()
        return redirect('listar_colaboradores')

    return render(request, 'colaboradores/editar.html', {
        'form': form
    })


def excluir_colaborador(request, id):

    colaborador = get_object_or_404(Colaborador, id=id)

    if request.method == 'POST':
        colaborador.delete()
        return redirect('listar_colaboradores')

    return render(request, 'colaboradores/excluir.html', {
        'colaborador': colaborador
    })