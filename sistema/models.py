# -*- coding: utf-8 -*-
from django.db import models
from ccbn.utils import generate_years_choice, read_all_models

class Modulo(models.Model):
    '''Modelo para definir los modulos a los que la persona va a estar asignada'''
    nombre = models.CharField(max_length=100)
    code = models.CharField(max_length=20, help_text='No cambiar este valor')

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = u'Módulos'
        permissions = (
            ("biblioteca", "Administrador Biblioteca"),
            ("formacion", "Administrador Formación"),
            ('atencion_integral', "Administrador Atención Integral"),
            ('promocion_artistica', "Administrador Promoción Artística"),
            ('pv_interna', "Administrador Prevención de Violencia Interna"),
            ('pv_externa', "Administrador Prevención de Violencia Externa"),
        )

# this list is based on the inlines with foo param in registro.admin module
INLINES = ('RegistroBibliotecaInline', 'FormacionBasicaInline', 'FormacionVocacionalInline', 'FormacionArtisticaInline',
           'RegistroBecaPrimariaInline', 'RegistroBecaSecundariaInline', 'RegistroBecaUniversitariaInline',
           'RegistroMusicaInline', 'RegistroTeatroInline', 'RegistroDanzaInline', 'RegistroCoroInline', 'RegistroPinturaInline')

class SubModulo(models.Model):
    '''Modelo para definir las subsecciones donde va a estar asignada la persona'''

    nombre = models.CharField(max_length=100)
    parent_module = models.ForeignKey(Modulo)
    code = models.CharField(max_length=20, help_text='No cambiar este valor')
    inline = models.CharField(max_length=100, choices=[(x, x) for x in INLINES])

    def __unicode__(self):
        return u'%s' % self.nombre

class Estrategia(models.Model):
    numero = models.CharField(max_length=100)
    nombre = models.TextField()
    programa = models.ForeignKey(Modulo)

    class Meta:
        verbose_name_plural = u'Estrategias'

    def __unicode__(self):
        return u'%s - %s' % (self.programa, self.nombre)

META_CHOICE = ((1, 'Percent'), (2, 'Count'))

def load_choice_models():
    return [('%s,%s' % (model._meta.app_label, model.__name__),
             '%s - %s' % (model._meta.app_label.title(), model._meta.verbose_name.title()))\
              for model in read_all_models()]    

class Salida(models.Model):
    year = models.IntegerField(choices=generate_years_choice(2012))
    estrategia = models.ForeignKey(Estrategia)
    meta = models.IntegerField(blank=True, null=True)
    titulo = models.TextField(blank=True, default='')
    tipo_meta = models.IntegerField(choices=META_CHOICE, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, default='', choices=load_choice_models())

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        ordering = ['estrategia__id', 'id']

    @models.permalink
    def get_absolute_url(self):
        return ('ccbn.views.salida_detail', [self.id])

    def meta_symbol(self):
        if self.tipo_meta == 1: # Percent
            return '%'
        elif self.tipo_meta == 2: # count
            return ''

CRITERIA_CHOICE = (('', 'None'), ('__gte', 'Mayor o igual que'), ('__gt', 'Mayor que'), 
                   ('__lte', 'Menor o igual que'), ('__lt', 'Menor que'))

class Filter(models.Model):
    salida = models.ForeignKey(Salida)
    field = models.CharField(max_length=50, default='')
    criteria = models.CharField(max_length=30, default='', choices=CRITERIA_CHOICE, blank=True)
    value = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % self.id

class QuerySplit(models.Model):
    salida = models.ForeignKey(Salida)
    field = models.CharField(max_length=50, default='')
    criteria = models.CharField(max_length=30, default='', choices=CRITERIA_CHOICE, blank=True)
    value = models.CharField(max_length=50)
    meta = models.IntegerField()
    tipo_meta = models.IntegerField(choices=META_CHOICE, blank=True, null=True)
    label = models.CharField(max_length=50, default='')

    def meta_symbol(self):
        if self.tipo_meta == 1: # Percent
            return '%'
        elif self.tipo_meta == 2: # count
            return ''

    def getlabel(self):
        if self.label != '':
            return self.label
        else:
            return self.field

    class Meta:
        verbose_name_plural = u'Query Split'

    def __unicode__(self):
        return u'%s' % self.id
