from django import forms
from .models import *

class TurnoForm(forms.ModelForm):
	class Meta:
		model = Turno
		fields = [
			'id',
			'nombre',
			'codigo',
			'inicio',
			'termino',
		]
        labels = {
			'id': 'id',
			'nombre': 'Nombre Jornada',
			'codigo': 'Codigo Jornnada ',
			'inicio': 'Hora de Inincio',
			'termino': 'Hora de Termino',
		}
        widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'codigo': forms.TextInput(attrs={'class':'form-control'}),
			'inicio': forms.TextInput(attrs={'class':'form-control'}),
			'termino': forms.TextInput(attrs={'class':'form-control'}),
		}   