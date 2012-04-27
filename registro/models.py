# -*- coding: utf-8 -*-
from django.db import models
from lugar.models import *
from sistema.models import *
from formacion.models import *
import datetime

SI_NO_CHOICE = ((1, 'Si'), (2, 'No'))
DISTRITO_CHOICE = ((1, u'Distrito 1'),
                   (2, u'Distrito 2'),
                   (3, u'Distrito 3'),
                   (4, u'Distrito 4'),
                   (5, u'Distrito 5'),
                   (6, u'Distrito 6'),
                   (99, u'No aplica'))
NIVEL_ACADEMICO_CHOICE = ((1, u'Pre-escolar'),
                          (2, u'No sabe leer ni escribir'),
                          (3, u'Alfabetizado'),
                          (4, u'Primaria incompleta'),
                          (5, u'Primaria completa'),
                          (6, u'Secundaria imcompleta'),
                          (7, u'Secundaria completa'),
                          (8, u'Técnico imcompleto'),
                          (9, u'Técnico completo'),
                          (10, u'Universidad imcompleta'),
                          (11, u'Universidad completa'),
                          (99, u'Ninguno'))
NIVEL_ESTUDIO_CHOICE = ((1, u'1er Grado'),
                        (2, u'2do Grado'),
                        (3, u'3er Grado'),
                        (4, u'4to Grado'),
                        (5, u'5to Grado'),
                        (6, u'6to Grado'),                         
                        (7, u'1er Año Secundaria'),
                        (8, u'2do Año Secundaria'),
                        (9, u'3er Año Secundaria'),
                        (10, u'4to Año Secundaria'),
                        (11, u'5to Año Secundaria'),                                                  
                        (13, u'1er Año Universidad'),
                        (14, u'2do Año Universidad'),
                        (15, u'3er Año Universidad'),
                        (18, u'4to Año Universidad'),
                        (19, u'5to Año Universidad'),
                        (16, u'Primaria Aprobada'),
                        (12, u'Bachiller'),                                                  
                        (20, u'Graduado Universidad'),                         
                        (21, u'Técnico/a'),
                        (17, u'Analfabeta'),
                        (22, u'Alfabetizado/a'))
JEFE_FAMILIA_CHOICE = ((1, u'Padre'),
                       (2, u'Madre'),
                       (3, u'Abuela'),
                       (4, u'Abuelo'),
                       (5, u'Pariente'),
                       (6, u'Hermano'),
                       (7, u'Hermana'),
                       (8, u'Institución'))

class Colegio(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name = u'Colegio/Centro de estudio'
        verbose_name_plural = u'Colegios/Centros de estudio'

class Oficio(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name = u'Oficio/Profesión'
        verbose_name_plural = u'Oficios/Profesiones'

class Pariente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = u'Parientes'

class Persona(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, default='')
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, default='')

    codigo = models.IntegerField(help_text=u'Autogenerado por el sistema')
    sexo = models.IntegerField(choices=((1, 'Masculino'), (2, 'Femenino')))
    fecha_nacimiento = models.DateField()
    cedula = models.CharField(max_length=20, blank=True, default='')

    personal_ccbn = models.IntegerField(choices=SI_NO_CHOICE)
    docente_ccbn = models.IntegerField(choices=SI_NO_CHOICE)

    municipio = models.ForeignKey(Municipio)
    ciudad = models.ForeignKey(Ciudad)
    barrio = models.ForeignKey(Barrio)
    distrito = models.IntegerField(choices=DISTRITO_CHOICE)

    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=12, help_text='Telefono convencional', blank=True, default='')
    celular = models.CharField(max_length=12, help_text='Telefono celular', blank=True, default='')

    nivel_academico = models.IntegerField(choices=NIVEL_ACADEMICO_CHOICE)
    nivel_estudio = models.IntegerField(choices=NIVEL_ESTUDIO_CHOICE)
    centro_actual = models.ForeignKey(Colegio, verbose_name = 'Centro de estudio actual', blank=True, null=True)
    oficio = models.ForeignKey(Oficio, blank=True, null=True)

    con_quien_vive = models.ManyToManyField(Pariente)
    tipo_familia = models.IntegerField() # todo: definir con don Falguni los tipos de familia

    jefe_familia = models.IntegerField(choices=JEFE_FAMILIA_CHOICE)
    j_primer_nombre = models.CharField(max_length=50, verbose_name = u'primer nombre')
    j_segundo_nombre = models.CharField(max_length=50, blank=True, default='', verbose_name = u'segundo nombre')
    j_primer_apellido = models.CharField(max_length=50, verbose_name = u'primer apellido')
    j_segundo_apellido = models.CharField(max_length=50, blank=True, default='', verbose_name = u'segundo apellido')
    j_oficio = models.ForeignKey(Oficio, related_name='oficio_jefe', blank=True, verbose_name = u'oficio', null=True)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.primer_nombre, self.segundo_nombre, 
                                 self.primer_apellido, self.segundo_apellido)

# 1: masculino, 2: femenino
RELACIONES = {
    'hermano': {1: 'hermano', 2: 'hermana'},
    'hermana': {1: 'hermano', 2: 'hermana'},
    'padre': {1: 'hijo', 2: 'hija'},
    'madre': {1: 'hijo', 2: 'hija'},
    'hijo': {1: 'padre', 2: 'madre'},
    'hija': {1: 'padre', 2: 'madre'},
    'primo': {1: 'primo', 2: 'prima'},
    'prima': {1: 'primo', 2: 'prima'},
    'abuelo': {1: 'nieto', 2: 'nieta'},
    'abuela': {1: 'nieto', 2: 'nieta'},
    'tio': {1: 'sobrino', 2: 'sobrina'},
    'tia': {1: 'sobrino', 2: 'sobrina'},
    'amigo': {1: 'amigo', 2: 'amiga'},
    'amiga': {1: 'amigo', 2: 'amiga'},
    'sobrina': {1: 'tio', 2: 'tia'},
    'sobrino': {1: 'tio', 2: 'tia'},
}

class Relacion(models.Model):
    parentesco = models.CharField(max_length=50, choices=[(key, key.title()) for key in RELACIONES.keys()])
    persona = models.ForeignKey(Persona, related_name='persona')
    owner = models.ForeignKey(Persona, related_name='owner')

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name = u'Relación'
        verbose_name_plural = u'Relaciones'

    # override para guardar la relacion con la otra persona
    def save(self, force_insert=False, force_update=False):
        super(Relacion, self).save(force_insert, force_update)

        # si force_update entonces la otra relacion ya se actualizo
        # retornar para evitar la recursion infinita :D
        if force_update:
            return

        try:
            obj = Relacion.objects.get(persona=self.owner, owner=self.persona)
            obj.parentesco = RELACIONES[self.parentesco][self.owner.sexo]
            obj.save(force_update=True)
        except:
            new_rel = Relacion()
            new_rel.owner = self.persona
            new_rel.persona = self.owner
            new_rel.parentesco = RELACIONES[self.parentesco][self.owner.sexo]
            new_rel.save()

class ModuloPersona(models.Model):
    biblioteca = models.ManyToManyField(SubModulo, related_name='biblioteca', blank=True, null=True,
                                         limit_choices_to = {'parent_module__code': 'module3'})
    formacion = models.ManyToManyField(SubModulo, related_name='formacion', blank=True, null=True,
                                       limit_choices_to = {'parent_module__code': 'module1'})
    atencion_integral = models.ManyToManyField(SubModulo, related_name='atencion_integral', blank=True, null=True,
                                                limit_choices_to = {'parent_module__code': 'module2'})
    promocion_artistica = models.ManyToManyField(SubModulo, related_name='promocion_artistica', blank=True, null=True,
                                                  limit_choices_to = {'parent_module__code': 'module4'})
    pv_interna = models.ManyToManyField(SubModulo, related_name='pv_interna',  limit_choices_to = {'parent_module__code': 'module5'},
                                        verbose_name = u'Prevención de Violencia Interna', blank=True, null=True,)
    pv_externa = models.ManyToManyField(SubModulo, related_name='pv_externa',  limit_choices_to = {'parent_module__code': 'module6'},
                                        verbose_name = u'Prevención de Violencia Externa', blank=True, null=True,)
    persona = models.OneToOneField(Persona)

    def __unicode__(self):
        return u'%s' % self.id

CHOICE_PORQUE_NO = ((1, u'No tiene interés'),
                    (2, u'Está trabajando'),
                    (3, u'Está estudiando'),
                    (4, u'Migró del país'),
                    (5, u'Cambio de domicilio'),
                    (6, u'Migro de municipio'),
                    (7, u'Fallecimiento'),
                    (8, u'Enfermedad'),
                    (9, u'Otros'))

class InscripcionCurso(models.Model):
    persona = models.ForeignKey(Persona)
    curso = models.ForeignKey(Curso)
    becado = models.IntegerField(choices=((1, u'Si'), (2, 'No')))
    fecha = models.DateField(verbose_name = u'Fecha de inscripcion', default=datetime.date.today())
    estado = models.IntegerField(verbose_name = u'Estado en curso', help_text='20%, 30%', blank=True, null=True)
    xq_no_termino = models.IntegerField(choices=CHOICE_PORQUE_NO, verbose_name = u'Porque no termino',
                                        blank=True, null=True)
    calificacion = models.IntegerField(help_text='Al final del curso', blank=True, null=True)
    mejora_autoestima = models.IntegerField(blank=True, null=True)  # TODO: integrar choices
    mejora_vida = models.IntegerField(blank=True, null=True)        # TODO: integrar choices
    calidad_contenido = models.IntegerField(blank=True, null=True)  # TODO: recordar que contenido va aca
    metodologia = models.IntegerField(blank=True, null=True)        # TODO: recordar contenido

    # solo para uso del sistema
    date_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return ''

    class Meta:
        verbose_name_plural = u'Inscripciones Cursos'

# Registro en Biblioteca, solo una vez
class RegistroBiblioteca(models.Model):
    fecha = models.DateField(default=datetime.date.today(), verbose_name = u'Fecha de registro')
    persona = models.OneToOneField(Persona)

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name_plural = u'Registros Biblioteca'

class BaseRegistroAnual(models.Model):
    persona = models.ForeignKey(Persona)
    fecha = models.DateField(default=datetime.date.today(), verbose_name = u'Fecha de registro')    

    def __unicode__(self):
        return u''

    class Meta:
        abstract = True

from atencionintegral.models import *

# Modelos de registro de becas, esto es año con año.
class RegistroBecaPrimaria(BaseRegistroAnual):
    beca = models.ForeignKey(BecaPrimaria, verbose_name = u'Beca primaria')
    tutoria = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    rendimiento_academico = models.IntegerField(blank=True, null=True)
    recibio_suplemento = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    recibio_atencion_psicologica = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    mejoro_habilidades = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    reconoce_capacidad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    perc_derecho = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)

    class Meta:
        verbose_name_plural = u'Registro Beca Primaria'

class RegistroBecaSecundaria(BaseRegistroAnual):
    beca = models.ForeignKey(BecaSecundaria, verbose_name = u'Beca secundaria')
    servicio_social = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    esp_propos = models.IntegerField(blank=True, null=True)
    promotor = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_famila = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_centro = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_comunidad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_sociedad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)

    class Meta:
        verbose_name_plural = u'Registro Beca Secundaria'

class RegistroBecaUniversitaria(BaseRegistroAnual):
    beca = models.ForeignKey(BecaUniversitaria, verbose_name = u'Beca universitaria')
    servicio_social = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    esp_propos = models.IntegerField(blank=True, null=True)
    promotor = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_famila = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_centro = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_comunidad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_sociedad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)    

    class Meta:
        verbose_name_plural = u'Registro Beca Universitaria'

# Modelos de registro en promocion artistica
class RegistroMusica(BaseRegistroAnual):
    class Meta:
        verbose_name_plural = u'Registro Grupo de Musica'

class RegistroTeatro(BaseRegistroAnual):
    class Meta:
        verbose_name_plural = u'Registro Grupo de Musica'

class RegistroDanza(BaseRegistroAnual):
    class Meta:
        verbose_name_plural = u'Registro Grupo de Danza'

class RegistroCoro(BaseRegistroAnual):
    class Meta:
        verbose_name_plural = u'Registro Grupo de Coro'

class RegistroPintura(BaseRegistroAnual):
    class Meta:
        verbose_name_plural = u'Registro Grupo de Pintura'
