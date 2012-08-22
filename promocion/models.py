# -*- coding: utf-8 -*-
from django.db import models
from atencionintegral.models import generate_years_choice, START_YEAR
from sistema.models import SubModulo

class BasePromocion(models.Model):
    nombre = models.CharField(max_length=100)
    semestre = models.IntegerField(choices=((1, '1er Semestre'), (2, '2do Semestre')))
    year = models.IntegerField('Año', choices=generate_years_choice(START_YEAR))

    def __unicode__(self):
        return u'%s %s %s' % (self.nombre, self.semestre, self.year)

    class Meta:
        abstract = True

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    semestre = models.IntegerField(choices=((1, '1er Semestre'), (2, '2do Semestre')))
    year = models.IntegerField('Año', choices=generate_years_choice(START_YEAR))
    submodulo = models.ForeignKey(SubModulo, verbose_name = u'Tipo', 
                                  limit_choices_to = {'parent_module__code': 'module4'})

    def __unicode__(self):
        return u'%s %s %s' % (self.nombre, self.get_semestre_display(), self.year)

    class Meta:
        verbose_name_plural = u'Grupos Artísticos'

CHOICE_ACTIVIDAD_COLECTIVA = ((1, u'Concierto de música'), (2, u'Coro'), (3, u'Exposición'),
                              (4, u'Obra de teatro'), (5, u'Multimedia'))

CHOICE_SENSIBILIZACION = ((1, 'Democracia'), (2, 'Participacion Ciudadana'), (3, 'Equidad de género'),
                          (4, 'Medio ambiente'), (5, 'Derechos Humanos'), (6, 'Solidaridad'))
CHOICE_APROPIACION = ((1, 'Excelente'), (2, 'Buena'), (3, 'Regular'), (4, 'Mala'))

class EventoColectivo(models.Model):
    fecha = models.DateTimeField()
    titulo = models.CharField('Nombre del evento', max_length=200)
    lugar = models.CharField(max_length=200)
    actividad = models.IntegerField(choices=CHOICE_ACTIVIDAD_COLECTIVA)

    participantes = models.IntegerField(default=0)
    ninos = models.IntegerField(default=0)
    ninas = models.IntegerField(default=0)
    jovenes_hombres = models.IntegerField(default=0)
    jovenes_mujeres = models.IntegerField(default=0)
    adultos_hombres = models.IntegerField(default=0)
    adultos_mujeres = models.IntegerField(default=0)

    sensibilizacion = models.IntegerField(verbose_name = u'Sensibilización del tema social',
                                          choices=CHOICE_SENSIBILIZACION)
    apropiacion = models.IntegerField(choices=CHOICE_APROPIACION)

    foto = models.ImageField(upload_to='biblioteca/activ_colectiva/', blank=True, null=True)
    comentarios = models.TextField(blank=True, default='')
    acuerdos = models.TextField(blank=True, default='')

    def __unicode__(self):
        return u'%s %s' % (self.actividad, self.fecha)

    class Meta:
        verbose_name_plural = u'Eventos Colectivos'