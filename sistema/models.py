from django.db import models

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