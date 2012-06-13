# -*- coding: utf-8 -*-
from django.db import models
from registro.models import CHOICE_CALIDAD, Persona

CHOICE_ACTIVIDADES_INTERNAS = ((1, 'Taller para CCBN'), (2, 'Taller para docentes'), (3, 'Taller para REDP'), 
                               (4, 'Grupos de Reflexión'), (5, 'Tema del mes'))
CHOICE_ACTIVIDADES_EXTERNAS = ((1, 'Feria'), (2, 'Charla'), (3, 'Reflexión'), (4, 'Lúdica'), (5, 'Teatro'))

CHOICE_TEMATICA = ((1, u'Derecho Niñez'), (2, u'Discriminación sexual'), (3, 'Violencia Intrafamiliar'),
                   (4, 'Derechos Humanos'), (5, 'Seguridad Ciudadana'))

class EventoInterno(models.Model):
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    actividad = models.IntegerField(choices=CHOICE_ACTIVIDADES_INTERNAS)

    participantes = models.IntegerField(default=0)
    tematica = models.IntegerField(choices=CHOICE_TEMATICA)
    metodologia = models.IntegerField(choices=CHOICE_CALIDAD)
    apropiacion = models.IntegerField(u'Apropiación y motivación', choices=CHOICE_CALIDAD)
    aprendizaje = models.IntegerField(choices=CHOICE_CALIDAD)
    participacion = models.IntegerField(choices=CHOICE_CALIDAD)

    foto = models.ImageField(upload_to='prevencion/evento_interno/', blank=True, null=True)
    comentarios = models.TextField(blank=True, default='')
    acuerdos = models.TextField(blank=True, default='')

    def __unicode__(self):
        return u'%s %s' % (self.actividad, self.fecha)

    class Meta:
        verbose_name_plural = u'Eventos Internos'

class EventoExterno(models.Model):
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    actividad = models.IntegerField(choices=CHOICE_ACTIVIDADES_EXTERNAS)

    facilitadores = models.IntegerField(default=0)
    ninos = models.IntegerField(default=0)
    ninas = models.IntegerField(default=0)
    jovenes_hombres = models.IntegerField(default=0)
    jovenes_mujeres = models.IntegerField(default=0)
    adultos_hombres = models.IntegerField(default=0)
    adultos_mujeres = models.IntegerField(default=0)

    tematica = models.IntegerField(choices=CHOICE_TEMATICA)

    foto = models.ImageField(upload_to='prevencion/evento_externo/', blank=True, null=True)
    comentarios = models.TextField(blank=True, default='')
    acuerdos = models.TextField(blank=True, default='')

    personas = models.ManyToManyField(Persona, limit_choices_to = {'modulopersona__pv_externa__gt': 0})

    def __unicode__(self):
        return u'%s %s' % (self.actividad, self.fecha)

    class Meta:
        verbose_name_plural = u'Eventos Externos'