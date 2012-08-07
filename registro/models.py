# -*- coding: utf-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey 
from lugar.models import *
from sistema.models import *
from formacion.models import *
from promocion.models import *
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
                          (6, u'Secundaria incompleta'),
                          (7, u'Secundaria completa'),
                          (8, u'Técnico incompleto'),
                          (9, u'Técnico completo'),
                          (10, u'Universidad incompleta'),
                          (11, u'Universidad completa'),
                          (99, u'Ninguno'))
NIVEL_ESTUDIO_CHOICE = (
                        (1, u'No estudia'),
                        (2, u'1er Nivel Preescolar'),
                        (3, u'2do Nivel Preescolar'),
                        (4, u'3er Nivel Preescolar'),
                        (5, u'1er Grado'),
                        (6, u'2do Grado'),
                        (7, u'3er Grado'),
                        (8, u'4to Grado'),
                        (9, u'5to Grado'),
                        (10, u'6to Grado'),                         
                        (11, u'1er Año Secundaria'),
                        (12, u'2do Año Secundaria'),
                        (13, u'3er Año Secundaria'),
                        (14, u'4to Año Secundaria'),
                        (15, u'5to Año Secundaria'),                                                  
                        (16, u'1er Año Universidad'),
                        (17, u'2do Año Universidad'),
                        (18, u'3er Año Universidad'),
                        (19, u'4to Año Universidad'),
                        (20, u'5to Año Universidad'),
                        (21, u'Alfabetizandose'),
                        (22, u'Técnico'),
                        (23, u'Postgrado'),
                        (24, u'Maestría'),
                        (25, u'Cursos'),
                        (26, u'Diplomados'),
                        )

TIPO_FAMILIA = ((1, u'Nuclear'),
    (2, u'Mono parental jefe hombre'),
    (3, u'Mono parental jefa mujer'),
    (4, u'Extendida'),
    (5, u'Ensamblada'))

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

    codigo = models.IntegerField(help_text=u'Autogenerado por el sistema', default=000)
    sexo = models.IntegerField(choices=((1, 'Masculino'), (2, 'Femenino')))
    fecha_nacimiento = models.DateField()
    cedula = models.CharField(max_length=20, blank=True, default='')
    
    # relacion con ccbn
    docente = models.BooleanField()
    personal = models.BooleanField()
    alumno = models.BooleanField()
    visitante = models.BooleanField()
    becado = models.BooleanField()
    promotor = models.BooleanField()
    beneficiario = models.BooleanField(verbose_name=u'Beneficiario de programa')
    integrante = models.BooleanField(verbose_name=u'Integrante promoción artística')
    
    municipio = models.ForeignKey(Municipio)
    ciudad = ChainedForeignKey(
        Ciudad, chained_field="municipio",
        chained_model_field="municipio", 
        show_all=False, auto_choose=True
    )
    barrio = ChainedForeignKey(
        Barrio, chained_field="ciudad", 
        chained_model_field="ciudad", 
        show_all=False, auto_choose=True
    )

    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=12, help_text='Telefono convencional', blank=True, default='')
    celular = models.CharField(max_length=12, help_text='Telefono celular', blank=True, default='')

    nivel_academico = models.IntegerField(choices=NIVEL_ACADEMICO_CHOICE)
    nivel_estudio = models.IntegerField('Estudio actual Externo', choices=NIVEL_ESTUDIO_CHOICE)
    centro_actual = models.ForeignKey(Colegio, verbose_name = 'Centro de estudio actual', blank=True, null=True)
    oficio = models.ForeignKey(Oficio, blank=True, null=True)

    con_quien_vive = models.ManyToManyField(Pariente, blank=True, null=True)
    tipo_familia = models.IntegerField(choices=TIPO_FAMILIA, blank=True, null=True)

    jefe_familia = models.IntegerField(choices=JEFE_FAMILIA_CHOICE)
    j_primer_nombre = models.CharField(max_length=50, verbose_name = u'primer nombre',
                                       blank=True, default='')
    j_segundo_nombre = models.CharField(max_length=50, blank=True, default='', verbose_name = u'segundo nombre')
    j_primer_apellido = models.CharField(max_length=50, verbose_name = u'primer apellido', blank=True, default='')
    j_segundo_apellido = models.CharField(max_length=50, blank=True, default='', verbose_name = u'segundo apellido')
    j_oficio = models.ForeignKey(Oficio, related_name='oficio_jefe', blank=True, verbose_name = u'oficio', null=True)

    def __unicode__(self):
        return u'%s - %s %s %s %s' % (self.codigo, self.primer_nombre, self.segundo_nombre, 
                                 self.primer_apellido, self.segundo_apellido)

    def save(self, *args, **kwargs):
        if not self.id:
            self.codigo = Persona.objects.all().count() + 1
        super(Persona, self).save(args, kwargs)

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
    'esposo': {1: 'esposo', 2: 'esposa'},
    'esposa': {1: 'esposo', 2: 'esposa'},
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

    pv_interna = models.ManyToManyField(SubModulo, related_name='pv_interna',  
                    limit_choices_to = {'parent_module__code': 'module5'},
                    verbose_name = u'Prevención de Violencia Interna', blank=True, null=True,)

    pv_externa = models.ManyToManyField(SubModulo, related_name='pv_externa',  
                    limit_choices_to = {'parent_module__code': 'module6'},
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
                    (9, u'Otros'),
                    (10, u'Si termino'))

CHOICE_ESTADO_CURSO = ((1, '10 %'), (2, '20 %'), (3, '30%'), (4, '40 %'), (5, '50 %'),
                       (6, '60 %'), (7, '70 %'), (8, '80 %'), (9, '90 %'), (10, '100 %'))
CHOICE_CALIFICACION = ((1, 'Paso'), (2, 'Regular'), (3, 'Bien'), (4, 'Excelente'), (5, 'No paso'))
CHOICE_MEJORA = ((1, 'Bastante'), (2, 'Algo'), (3, 'Poco'), (4, 'Nada'))
CHOICE_MEJORA_VIDA = ((1, u'Muy útil'), (2, u'Útil'), (3, u'Poco útil'), (4, u'Nada útil'))
CHOICE_CALIDAD = ((1, 'Excelente'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'))
CHOICE_METODOLOGIA = CHOICE_CALIDAD
CHOICE_APORTE = ((1, u'Muy útil'), (2, u'Útil'), (3, u'Poco útil'), (4, u'Nada útil'))
CHOICE_CONTINUA_EST = ((1, 'Si'), (2, 'No'), (3, 'No aplica'))

class InscripcionCurso(models.Model):
    persona = models.ForeignKey(Persona)
    curso = models.ForeignKey(Curso)
    becado = models.IntegerField(choices=((1, u'Si'), (2, 'No')))
    fecha = models.DateField(verbose_name = u'Fecha de inscripcion', default=datetime.date.today())
    estado = models.IntegerField(verbose_name = u'Estado en curso', help_text='20%, 30%', 
                                 blank=True, null=True, choices=CHOICE_ESTADO_CURSO)
    xq_no_termino = models.IntegerField(choices=CHOICE_PORQUE_NO, verbose_name = u'Porque no termino',
                                        blank=True, null=True)
    calificacion = models.IntegerField(help_text='Al final del curso', 
                                       blank=True, null=True, choices=CHOICE_CALIFICACION)
    mejora_autoestima = models.IntegerField(blank=True, null=True, choices=CHOICE_MEJORA)
    aporte_sociedad = models.IntegerField(blank=True, null=True, choices=CHOICE_APORTE, verbose_name=u'Aporte a sociedad, familia y comunidad')
    mejora_vida = models.IntegerField(blank=True, null=True, choices=CHOICE_MEJORA_VIDA)
    calidad_contenido = models.IntegerField(blank=True, null=True, choices=CHOICE_CALIDAD)
    metodologia = models.IntegerField(blank=True, null=True, choices=CHOICE_METODOLOGIA)
    continua_estudiando = models.IntegerField(choices=CHOICE_CONTINUA_EST, blank=True, null=True, 
                                help_text=u'En curso vocacional o secundaria. Aplica para educación primaria finalizada')

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
    esp_propos = models.IntegerField(blank=True, null=True, verbose_name=u'Espíritu propositivo')
    promotor = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_famila = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_centro = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_comunidad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_sociedad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    bibliotecario =  models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = u'Registro Beca Secundaria'

class RegistroBecaUniversitaria(BaseRegistroAnual):
    beca = models.ForeignKey(BecaUniversitaria, verbose_name = u'Beca universitaria')
    servicio_social = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    esp_propos = models.IntegerField(choices=SI_NO_CHOICE,blank=True, null=True, verbose_name=u'Espíritu propositivo')
    promotor = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_famila = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_centro = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_comunidad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    solidario_sociedad = models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)
    bibliotecario =  models.IntegerField(choices=SI_NO_CHOICE, blank=True, null=True)   

    class Meta:
        verbose_name_plural = u'Registro Beca Universitaria'

CHOICE_VALORES_CCBN = ((1, 'Avanzado'), (2, 'Iniciado'), (3, 'No Iniciado'))

class BaseRegistroPromocion(BaseRegistroAnual):
    asistencia = models.IntegerField(blank=True, null=True, choices=CHOICE_ESTADO_CURSO)
    razon_no_continuar = models.IntegerField(blank=True, null=True, choices=CHOICE_PORQUE_NO)
    calificacion = models.IntegerField(blank=True, null=True, choices=CHOICE_CALIFICACION)
    valores_ccbn = models.IntegerField(blank=True, null=True, choices=CHOICE_VALORES_CCBN)
    genero = models.IntegerField(blank=True, null=True, choices=CHOICE_VALORES_CCBN)
    mejora_capacidad = models.IntegerField(blank=True, null=True, choices=CHOICE_MEJORA)
    utilidad_para_vida = models.IntegerField(blank=True, null=True, choices=CHOICE_MEJORA_VIDA)
    calidad_creativa = models.IntegerField(blank=True, null=True, choices=CHOICE_CALIDAD)
    metodologia = models.IntegerField(blank=True, null=True, choices=CHOICE_CALIDAD)
    perspectiva = models.IntegerField(blank=True, null=True, choices=CHOICE_CALIDAD)

    class Meta:
        abstract = True

# Modelos de registro en promocion artistica
class RegistroMusica(BaseRegistroPromocion):
    grupo = models.ForeignKey(Musica)
    class Meta:
        verbose_name_plural = u'Registro Grupo de Musica'

class RegistroTeatro(BaseRegistroPromocion):
    grupo = models.ForeignKey(Teatro)
    class Meta:
        verbose_name_plural = u'Registro Grupo de Musica'

class RegistroDanza(BaseRegistroPromocion):
    grupo = models.ForeignKey(Danza)
    class Meta:
        verbose_name_plural = u'Registro Grupo de Danza'

class RegistroCoro(BaseRegistroPromocion):
    grupo = models.ForeignKey(Coro)
    class Meta:
        verbose_name_plural = u'Registro Grupo de Coro'

class RegistroPintura(BaseRegistroPromocion):
    grupo = models.ForeignKey(Pintura)
    class Meta:
        verbose_name_plural = u'Registro Grupo de Pintura'