from django import forms
from .models import *
class TurnoForm(forms.ModelForm):
	class Meta:
		model = Turno
		fields = [
			'id',
			'nombre',
			'codigo',
            'dias',
			'inicio',
			'termino',
            
		]
        widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'dias': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
			'inicio': forms.TextInput(attrs={'class':'form-control'}),
			'termino': forms.TextInput(attrs={'class':'form-control'}),
		}