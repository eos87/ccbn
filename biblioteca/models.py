# -*- coding: utf-8 -*-
from django.db import models
from registro.models import Persona

class ActividadIndividual(models.Model):
    persona = models.ForeignKey(Persona)
    fecha = models.DateTimeField()
    actividad = models.IntegerField()

    # actividad == prestamo
    class Meta:
        abstract = True

class ActividadColectiva(models.Model):
    fecha = models.DateTimeField()
    actividad = models.IntegerField() # with choices
    ninos = models.IntegerField()
    ninas = models.IntegerField()
    jovenes_hombres = models.IntegerField()
    jovenes_mujeres = models.IntegerField()
    adultos_hombres = models.IntegerField()
    adultos_mujeres = models.IntegerField()

    evaluacion_rapida = models.TextField()
    foto = models.ImageField(upload_to='biblioteca/activ_colectiva/', blank=True, null=True)
    comentarios = models.TextField(blank=True, default='')
    acuerdos = models.TextField(blank=True, default='')

    def __unicode__(self):
        return u''

    class Meta:
        verbose_name_plural = u'Actividades Colectivas'