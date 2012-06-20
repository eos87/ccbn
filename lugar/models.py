# -*- coding: UTF-8 -*-

from django.db import models

class Departamento(models.Model):
    id = models.IntegerField("Código", primary_key=True)
    nombre = models.CharField(max_length=30, unique= True)
    slug = models.SlugField(unique=True, null=True, help_text="Usado como url unica(autorellenado)")
    extension = models.DecimalField("Extension Territorials", max_digits=10,decimal_places=2, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Departamentos"

class Municipio(models.Model):
    id = models.IntegerField("Código", primary_key=True)
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, null=True, help_text="Usado como url unica(autorellenado)")
    extension = models.DecimalField("Extension Territorial", max_digits=10, decimal_places=2, blank=True, null=True)
    latitud = models.DecimalField('Latitud', max_digits=8, decimal_places=5, blank=True, null = True)
    longitud = models.DecimalField('Longitud', max_digits=8, decimal_places=5, blank=True, null = True)

    def __unicode__(self):
        return '%s - %s' % (self.departamento.nombre, self.nombre)

    class Meta:
        verbose_name_plural = "Municipios"
        ordering = ['departamento__nombre',]

CIUDAD_TIPO = ((1, 'Ciudad'), (2, 'Comunidad'))

class Ciudad(models.Model):
    municipio = models.ForeignKey(Municipio)
    tipo = models.IntegerField(choices=CIUDAD_TIPO)
    nombre = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Ciudad/Comunidad'
        verbose_name_plural = 'Ciudades/Comunidades'

    def __unicode__(self):
        return self.nombre

BARRIO_TIPO = ((1, 'Barrio'), (2, 'Comarca'))
DISTRITO_TIPO = ((1, 'Distrito 1'), (2, 'Distrito 2'),
                 (3, 'Distrito 3'), (4, 'Distrito 4'),
                 (5, 'Distrito 5'), (6, 'Distrito 6'))

class Barrio(models.Model):
    ciudad = models.ForeignKey(Ciudad)
    tipo = models.IntegerField(choices=BARRIO_TIPO)
    nombre = models.CharField(max_length=40)
    distrito = models.IntegerField(choices=DISTRITO_TIPO)
    class Meta:
        verbose_name = 'Barrio/Comarca'
        verbose_name_plural = 'Barrios/Comarcas'

    def __unicode__(self):
        return self.nombre
