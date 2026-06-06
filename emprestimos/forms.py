from django import forms
from django.utils import timezone
from .models import Emprestimo


class EmprestimoForm(forms.ModelForm):

    class Meta:
        model = Emprestimo
        fields = [
            'colaborador',
            'equipamento',
            'data_prevista_devolucao',
            'status',
            'data_devolucao',
            'observacao_devolucao',
        ]

        widgets = {
            'data_prevista_devolucao': forms.DateInput(attrs={'type': 'date'}),
            'data_devolucao': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # CADASTRO
        if not self.instance.pk:
            self.fields['status'].choices = [
                ('EMPRESTADO', 'Emprestado'),
                ('FORNECIDO', 'Fornecido'),
            ]

        # EDIÇÃO
        else:
            self.fields['colaborador'].disabled = True
            self.fields['equipamento'].disabled = True
            self.fields['data_prevista_devolucao'].disabled = True

    def clean_data_prevista_devolucao(self):
        data = self.cleaned_data['data_prevista_devolucao']

        if data <= timezone.now():
            raise forms.ValidationError(
                'A data prevista de devolução deve ser futura.'
            )

        return data