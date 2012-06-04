from django.db import models
from ccbn.utils import generate_years_choice, read_all_models

class Modulo(models.Model):
    '''Modelo para definir los modulos a los que la persona va a estar asignada'''
    nombre = models.CharField(max_length=100)
    code = models.CharField(max_length=20, help_text='No cambiar este valor')

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = u'Modulos'

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

META_CHOICE = ((1, 'Percent'), (2, 'Count'))

def load_choice_models():
    return [('%s,%s' % (model._meta.app_label, model.__name__),
             '%s - %s' % (model._meta.app_label.title(), model._meta.verbose_name.title()))\
              for model in read_all_models()]    

class Salida(models.Model):
    year = models.IntegerField(choices=generate_years_choice(2012))
    meta = models.IntegerField(blank=True, null=True)
    titulo = models.TextField(blank=True, default='')
    tipo_meta = models.IntegerField(choices=META_CHOICE, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, default='', choices=load_choice_models())

    def __unicode__(self):
        return u'%s' % self.id

    def meta_symbol(self):
        if self.tipo_meta == 1: # Percent
            return '%'
        elif self.tipo_meta == 2: # count
            return ''

CRITERIA_CHOICE = (('', 'None'), ('__gte', 'greater than or equal'), )

class Filter(models.Model):
    salida = models.ForeignKey(Salida)
    field = models.CharField(max_length=50, blank=True, default='', choices=((1,1), ))
    criteria = models.CharField(max_length=30, blank=True, default='', choices=CRITERIA_CHOICE)
    value = models.CharField(max_length=50, blank=True, default='')

    def __unicode__(self):
        return u'%s' % self.id
