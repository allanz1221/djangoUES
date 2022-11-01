from django import forms
from fisioterapias.models import Cita

class AddCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = {'motivo'}
        labels = {
            'motivo': 'MOTIVO'
        }
