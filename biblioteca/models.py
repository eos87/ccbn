# -*- coding: utf-8 -*-
from django.db import models
from registro.models import Persona

CHOICE_ACTIVIDAD = (('ConsultaInline', u'Consulta de libros'),
                    ('PrestamoInline', u'Prestamo de libro'),
                    ('RetornoInline', u'Retorno de libro'),
                    ('ServicioInline', u'Servicio Bibliotecario'))

CHOICE_CATEGORIA = ((1, u'000 - Generalidades'), (2, u'100 - Filosofía y Psicología'),
                    (3, u'200 - Religión'), (4, u'300 - Ciencias Sociales'),
                    (5, u'400 - Lenguas'), (6, u'500 - Ciencias Puras'),
                    (7, u'600 - Ciencias Aplicadas'), (8, u'700 - Arte'),
                    (9, u'800 - Literatura'), (10, u'900 - Geografía e Historia'))

CHOICE_PROPOSITO = ((1, u'Investigación'), (2, u'Hábito de lectura'))

class ActividadIndividual(models.Model):
    persona = models.ForeignKey(Persona)
    fecha = models.DateTimeField()
    actividad = models.CharField(choices=CHOICE_ACTIVIDAD, max_length=100)

    def __unicode__(self):
        return u'Registro el %s' % self.fecha

    def _get_display(self):
        return '%s | %s' % (self.get_actividad_display(), self.persona)

    display = property(_get_display)

    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = u'Actividades Individuales'

class Consulta(models.Model):
    actividad = models.ForeignKey(ActividadIndividual)
    categoria = models.IntegerField(choices=CHOICE_CATEGORIA)
    proposito = models.IntegerField(choices=CHOICE_PROPOSITO)

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name_plural = u'Consultas'

class Libro(models.Model):
    categoria = models.IntegerField(choices=CHOICE_CATEGORIA)
    registro = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.registro

    class Meta:
        verbose_name_plural = u'Libros'

class Prestamo(models.Model):
    actividad = models.ForeignKey(ActividadIndividual)
    libro = models.ForeignKey(Libro)
    dias = models.IntegerField(u'Días de préstamo')
    fecha_retorno = models.DateField()

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name_plural = u'Prestamos'

class Retorno(models.Model):
    actividad = models.ForeignKey(ActividadIndividual)
    libro = models.ForeignKey(Libro)
    dias_mora = models.IntegerField()
    fecha_retorno = models.DateField()

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name_plural = u'Retornos'

class Servicio(models.Model):
    actividad = models.ForeignKey(ActividadIndividual)
    capacidad_tecnica = models.IntegerField()
    compromiso_social = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name = u'Servicio Bibliotecario'
        verbose_name_plural = u'Servicios bibliotecarios'


class ActividadColectiva(models.Model):
    fecha = models.DateTimeField()
    actividad = models.IntegerField() # with choices
    ninos = models.IntegerField(default=0)
    ninas = models.IntegerField(default=0)
    jovenes_hombres = models.IntegerField(default=0)
    jovenes_mujeres = models.IntegerField(default=0)
    adultos_hombres = models.IntegerField(default=0)
    adultos_mujeres = models.IntegerField(default=0)

    evaluacion_rapida = models.TextField()
    foto = models.ImageField(upload_to='biblioteca/activ_colectiva/', blank=True, null=True)
    comentarios = models.TextField(blank=True, default='')
    acuerdos = models.TextField(blank=True, default='')

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name_plural = u'Actividades Colectivas'