from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TurnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(TurnoForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', u'Save'))


    # I think so that here is my problem ...

    def save(self, commit=True):

        nombre_turno = super(TurnoForm, self).save(commit=False)

        nombre = self.cleaned_data['nombre']


        if commit:

            nombre_turno.save()

        return nombre_turno

	class Meta:
		model = Turno
		fields = [
			'id',
			'nombre',
			'codigo',
			'inicio',
			'termino',
		] 