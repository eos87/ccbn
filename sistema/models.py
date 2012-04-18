from django.db import models
from django.utils.importlib import import_module

def classes_to_choices(module, attr):
    choices = []
    try:
        module = import_module(module)
    except Exception as e:
        print e
    for obj in dir(module):
        klass = getattr(module, obj)
        if hasattr(klass, attr):
            option = (klass.__class__.__name__, klass.__class__.__name__)
            if option not in choices:
                choices.append(option)
    return choices

class Modulo(models.Model):
    '''Modelo para definir los modulos a los que la persona va a estar asignada'''
    nombre = models.CharField(max_length=100)
    code = models.CharField(max_length=20, help_text='No cambiar este valor')

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = u'Modulos'

class SubModulo(models.Model):
    '''Modelo para definir las subsecciones donde va a estar asignada la persona'''

    nombre = models.CharField(max_length=100)
    parent_module = models.ForeignKey(Modulo)
    code = models.CharField(max_length=20, help_text='No cambiar este valor')
    inline = models.CharField(max_length=100, choices=(('1', 'll'), ('2', 'lll3'))) # classes_to_choices('registro.admin', 'foo'))

    def __unicode__(self):
        return u'%s' % self.nombre