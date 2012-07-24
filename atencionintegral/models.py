# -*- coding: utf-8 -*-
from django.db import models
from ccbn.utils import generate_years_choice
import datetime
#from promocion.models import CHOICE_SENSIBILIZACION, CHOICE_APROPIACION

CHOICE_SENSIBILIZACION = ((1, 'Democracia'), (2, 'Participación Ciudadana'), (3, 'Equidad de genero'),
                          (4, 'Medio ambiente'), (5, 'Derechos Humanos'), (6, 'Solidaridad'))
CHOICE_APROPIACION = ((1, 'Excelente'), (2, 'Buena'), (3, 'Regular'), (4, 'Mala'))

START_YEAR = 2012

class BaseBeca(models.Model):
    year = models.IntegerField('Año de beca', choices=generate_years_choice(START_YEAR))

    def __unicode__(self):
        return u'Beca del año %s' % self.year

    class Meta:
        abstract = True

class BecaPrimaria(BaseBeca):
    class Meta:
        verbose_name_plural = u'Becas de Primaria'

class BecaSecundaria(BaseBeca):
    class Meta:
        verbose_name_plural = u'Becas de Secundaria'

class BecaUniversitaria(BaseBeca):
    class Meta:
        verbose_name_plural = u'Becas Universitarias'

class ActividadEventoAtencion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de actividad"

class EventoColectivoAtencion(models.Model):
    fecha = models.DateTimeField()
    titulo = models.CharField('Nombre del evento', max_length=200)
    lugar = models.CharField(max_length=200)
    actividad = models.ForeignKey(ActividadEventoAtencion, verbose_name="Actividad")

    participantes = models.IntegerField(default=0)
    ninos = models.IntegerField(default=0)
    ninas = models.IntegerField(default=0)
    jovenes_hombres = models.IntegerField(default=0)
    jovenes_mujeres = models.IntegerField(default=0)
    adultos_hombres = models.IntegerField(default=0)
    adultos_mujeres = models.IntegerField(default=0)

    sensibilizacion = models.IntegerField(verbose_name = u'Sensibilización del tema social',
                                          choices=CHOICE_SENSIBILIZACION,
                                          blank=True, null=True)
    apropiacion = models.IntegerField(choices=CHOICE_APROPIACION)

    foto = models.ImageField(upload_to='biblioteca/activ_colectiva/', blank=True, null=True)
    comentarios = models.TextField(blank=True, default='')
    acuerdos = models.TextField(blank=True, default='')

    def __unicode__(self):
        return u'%s %s' % (self.actividad, self.fecha)

    class Meta:
        verbose_name_plural = u'Eventos colectivos de atención integral'
