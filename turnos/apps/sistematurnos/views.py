# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from .models import *
from .form import TurnoForm



# Create your views here.
class TurnoCreate(CreateView):
	model = Turno
	form_class = TurnoForm
	template_name = 'sistematurno/turno_form.html'
	success_url = reverse_lazy('sistematurnos:Turno_listar')


class TurnoList(ListView):
	queryset = Turno.objects.order_by('id')
	template_name = 'sistematurno/turno_list.html'
class TurnoUpdate(UpdateView):
	model = Turno
	form_class = TurnoForm
	template_name = 'sistematurno/turno_form.html'
	success_url = reverse_lazy('sistematurnos:Turno_listar')

class TurnoDelete(DeleteView):
	model = Turno
	template_name = 'sistematurno/turno_delete.html'
	success_url = reverse_lazy('sistematurnos:Turno_listar')

class TurnoShow(DetailView):
	model = Turno
	template_name = 'sistematurno/turno_show.html'