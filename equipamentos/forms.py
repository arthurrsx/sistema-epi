from django import forms
from .models import Equipamento


class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = '__all__'
        widgets = {
            'validade': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.setdefault(
                'class',
                'form-control'
            )