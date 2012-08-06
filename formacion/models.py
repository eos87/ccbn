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

PRIMARIA_CHOICE = ((1, u'1er Año'), (2, u'2do Año'), (3, u'3er Año'), (4, 'No aplica'))

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    frecuencia = models.ForeignKey(Frecuencia)
    horario = models.IntegerField(choices=CHOICE_HORARIO)

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    submodulo = models.ForeignKey(SubModulo, verbose_name = u'Área', limit_choices_to = {'parent_module__code': 'module1'})
    primaria_year = models.IntegerField(choices=PRIMARIA_CHOICE, default=4,
                                        verbose_name=u'Año de primaria', help_text=u'Aplica solo para educación básica (primaria)')

    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.nombre, self.fecha_inicio.strftime("%d/%m/%Y"), self.frecuencia, self.get_horario_display())

    class Meta:
        verbose_name_plural = u'Cursos'

CHOICE_EVAL = ((1, 'Excelente'), (2, 'Buena'), (3, 'Regular'), (4, 'Mala'))
CHOICE_EVAL_GENERO = ((1, 'Avanzado'), (2, 'Iniciado'), (3, 'No iniciado'))

class EvaluacionCurso(models.Model):
    curso = models.OneToOneField(Curso)
    calidad_contenido = models.IntegerField(choices=CHOICE_EVAL)
    metodologia = models.IntegerField(choices=CHOICE_EVAL)
    calificacion_docente = models.IntegerField(choices=CHOICE_EVAL)
    genero = models.IntegerField(choices=CHOICE_EVAL_GENERO)

    def __unicode__(self):
        return u'Evaluación curso %s' % self.curso.nombre

    class Meta:
        verbose_name = u'Evaluación de curso'
        verbose_name_plural = u'Evaluación de cursos'

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
