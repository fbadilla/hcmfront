# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import myFields

# Create your models here.
class Dia(models.Model):
	id = models.AutoField(primary_key=True)
	dia = models.CharField(max_length=30, default="")
	def __str__(self):
		return '{}'.format(self.dia)

class Turno(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=70)
	codigo = models.CharField(max_length=70, default='' )
	inicio = models.TimeField( blank=True, null=True)
	termino = models.TimeField( blank=True, null=True)
	dias = models.ManyToManyField(Dia)
	def __str__(self):
		return '{}'.format(self.nombre)