from django import forms
from fisioterapias.models import Cita

class AddCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = {'aula', 'motivo', 'cumplio','costo', 'paciente'}
        labels = {
            'aula':'aula', 
            'motivo':'motivo', 
            'cumplio':'cumplio',
            'costo':'costo', 
            'paciente':'paciente'
            
        }
