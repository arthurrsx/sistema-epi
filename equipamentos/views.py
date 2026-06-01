from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento
from .forms import EquipamentoForm


def listar_equipamentos(request):

    equipamentos = Equipamento.objects.all()

    return render(request, 'equipamentos/listar.html', {
        'equipamentos': equipamentos
    })


def cadastrar_equipamento(request):

    form = EquipamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_equipamentos')

    return render(request, 'equipamentos/cadastrar.html', {
        'form': form
    })


def editar_equipamento(request, id):

    equipamento = get_object_or_404(
        Equipamento,
        id=id
    )

    form = EquipamentoForm(
        request.POST or None,
        instance=equipamento
    )

    if form.is_valid():
        form.save()
        return redirect('listar_equipamentos')

    return render(request, 'equipamentos/editar.html', {
        'form': form
    })


def excluir_equipamento(request, id):

    equipamento = get_object_or_404(
        Equipamento,
        id=id
    )

    if request.method == 'POST':
        equipamento.delete()
        return redirect('listar_equipamentos')

    return render(request, 'equipamentos/excluir.html', {
        'equipamento': equipamento
    })