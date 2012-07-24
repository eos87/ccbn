# -*- coding: utf-8 -*-
from django.db import models
from sistema.models import SubModulo
#from promocion.models import CHOICE_APROPIACION, CHOICE_SENSIBILIZACION

CHOICE_SENSIBILIZACION = ((1, 'Democracia'), (2, 'Participación Ciudadana'), (3, 'Equidad de género'),
                          (4, 'Medio ambiente'), (5, 'Derechos Humanos'), (6, 'Solidaridad'))
CHOICE_APROPIACION = ((1, 'Excelente'), (2, 'Buena'), (3, 'Regular'), (4, 'Mala'))

CHOICE_HORARIO = ((1, u'Matutino'), 
                  (2, u'Vespertino'),
                  (3, u'Nocturno'))

class Frecuencia(models.Model):
    nombre = models.CharField(max_length=300)
    cantidad = models.IntegerField(verbose_name = u'Cantidad de días')

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = u'Frecuencias'

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    frecuencia = models.ForeignKey(Frecuencia)
    horario = models.IntegerField(choices=CHOICE_HORARIO)

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    submodulo = models.ForeignKey(SubModulo, verbose_name = u'Área', limit_choices_to = {'parent_module__code': 'module1'})

    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.nombre, self.fecha_inicio.strftime("%d/%m/%Y"), self.frecuencia, self.get_horario_display())

    class Meta:
        verbose_name_plural = u'Cursos'

class ActividadEventoFormacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de actividad"

class EventoColectivoFormacion(models.Model):
    fecha = models.DateTimeField()
    titulo = models.CharField('Nombre del evento', max_length=200)
    lugar = models.CharField(max_length=200)
    actividad = models.ForeignKey(ActividadEventoFormacion, verbose_name="Actividad")

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
        verbose_name_plural = u'Eventos colectivos de formación'
