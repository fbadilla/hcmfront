# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-17 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistematurnos', '0002_auto_20200214_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='turno',
            name='codigo',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='turno',
            name='dias',
            field=models.ManyToManyField(to='sistematurnos.Dia'),
        ),
    ]