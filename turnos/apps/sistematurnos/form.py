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
