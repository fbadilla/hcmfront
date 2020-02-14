# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Turno(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=70)
    codigo = models.CharField(max_length=70)
	inicio = models.TimeField(['%I:%H %p'], blank=True, null=True)
	termino = models.TimeField(['%I:%H %p'], blank=True, null=True)
	def __str__(self):
		return '{}'.format(self.nombre)
