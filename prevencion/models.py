# -*- coding: utf-8 -*-
from django.db import models
from registro.models import (CHOICE_CALIDAD, CHOICE_ESTADO_CURSO, CHOICE_CALIFICACION, 
                             Persona)
from ccbn.utils import generate_years_choice
import datetime

CHOICE_ACTIVIDADES_INTERNAS = (
                               (1, 'Taller para CCBN'), 
                               (2, 'Taller para docentes'), 
                               (3, 'Taller para RPSC'), 
                               (4, 'Grupos de Reflexión'), 
                               (5, 'Campañas'), 
                               (6, 'Ferias'), 
                               (7, 'Fortalecimiento institucional'),
                               (8, 'Intercambios'),
                               (9, 'Foro'),
                               (10, 'Lúdica'),
                               (11, 'Teatro'),
                               (12, 'Charlas'),
                               (13, 'Autocuido'),
                               (14, 'Autoayuda'),
                               )

CHOICE_TEMATICA = ((1, u'Derecho Niñez'), 
                   (2, u'Discriminación'), 
                   (3, 'Violencia Intrafamiliar'),
                   (4, 'Derechos Humanos'), 
                   (5, 'Violencia basada en género'),
                   (6, 'Autoestima'),
                   (7, 'Liderazgo'),
                   (8, 'Incidencia Política'),
                   (9, 'Autocuido'),
                   )

class EventoInterno(models.Model):
    fecha = models.DateTimeField()
    titulo = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    actividad = models.IntegerField(choices=CHOICE_ACTIVIDADES_INTERNAS)

    participantes = models.IntegerField(default=0)
    ninos = models.IntegerField(default=0)
    ninas = models.IntegerField(default=0)
    jovenes_hombres = models.IntegerField(default=0)
    jovenes_mujeres = models.IntegerField(default=0)
    adultos_hombres = models.IntegerField(default=0)
    adultos_mujeres = models.IntegerField(default=0)
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
    titulo = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    actividad = models.IntegerField(choices=CHOICE_ACTIVIDADES_INTERNAS)

    facilitadores = models.IntegerField("Participantes",default=0, null=True, blank=True)
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

    personas = models.ManyToManyField(Persona, blank=True,
               limit_choices_to = {'modulopersona__pv_externa__gt': 0})

    def __unicode__(self):
        return u'%s %s' % (self.actividad, self.fecha)

    class Meta:
        verbose_name_plural = u'Eventos Externos'

CHOICE_SEMESTRE = ((1, '1er Semestre'), (2, '2do Semestre'))
CHOICE_ACTOR_CCBN = ((1, 'Personal CCBN'), (2, 'Docentes CCBN'), (3, 'Promotores/as'))

class PrevencionInterna(models.Model):
    year = models.IntegerField('Año', choices=generate_years_choice(2012))
    semestre = models.IntegerField(choices=CHOICE_SEMESTRE)
    relacion_ccbn = models.IntegerField(choices=CHOICE_ACTOR_CCBN)

    def __unicode__(self):
        return u'%s %s %s' % (
                self.get_relacion_ccbn_display(),
                self.get_semestre_display(), 
                self.year
        )

    class Meta:
        verbose_name = u'Prevención Interna'
        verbose_name_plural = u'Prevención Interna'

CHOICE_NO_ASISTIR = ((1, 'Social'), (2, u'Económico'), (3, u'Conducta'), (4, u'Falta de interés'))
CHOICE_AUTOEST = ((1, 'No iniciado'), (2, u'Iniciado'), (3, u'Avanzado'), (4, 'Logrado'))

class InscripcionPrevencionInterna(models.Model):
    persona = models.ForeignKey(Persona)
    pvbg_interna = models.ForeignKey(PrevencionInterna)
    fecha = models.DateField(verbose_name = u'Fecha de inscripcion', default=datetime.date.today())

    asistencia = models.IntegerField(choices=CHOICE_ESTADO_CURSO, blank=True, null=True,
            verbose_name=u'Asistencia en Talleres PVBG')
    razon_no_asistir = models.IntegerField(choices=CHOICE_NO_ASISTIR, blank=True, null=True)
    calificacion = models.IntegerField(choices=CHOICE_CALIFICACION, blank=True, null=True)
    mejora_autoestima = models.IntegerField(choices=CHOICE_AUTOEST, blank=True, null=True)
    nivel_conocimiento = models.IntegerField(choices=CHOICE_AUTOEST, blank=True, null=True, 
            help_text=u'Nivel de conocimiento de prevención de VBG')
    calidad_contenido = models.IntegerField(choices=CHOICE_CALIDAD, blank=True, null=True)
    metodologia = models.IntegerField(choices=CHOICE_CALIDAD, blank=True, null=True)
    empoderamiento = models.IntegerField(choices=CHOICE_CALIDAD, blank=True, null=True,
            verbose_name=u'Empoderamiento y acción comunitaria')

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name_plural = u'Inscripciones Prevencion Interna'
