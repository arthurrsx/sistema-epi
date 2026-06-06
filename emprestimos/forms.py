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
            'data_prevista_devolucao': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'data_devolucao': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_prevista_devolucao'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['data_devolucao'].input_formats = ['%Y-%m-%dT%H:%M']

        # 🔥 bloqueia edição (mantido como você já tinha)
        if self.instance.pk:
            self.fields['colaborador'].disabled = True
            self.fields['equipamento'].disabled = True
            self.fields['data_prevista_devolucao'].disabled = True

        else:
            self.fields['status'].choices = [
                ('EMPRESTADO', 'Emprestado'),
                ('FORNECIDO', 'Fornecido'),
            ]

    def clean_data_prevista_devolucao(self):
        data = self.cleaned_data.get('data_prevista_devolucao')

        if data:
            if timezone.is_naive(data):
                data = timezone.make_aware(data)

            if data <= timezone.now():
                raise forms.ValidationError(
                    "A data prevista deve ser futura."
                )

        return data