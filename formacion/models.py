from django.db import models
from sistema.models import SubModulo

CHOICE_HORARIO = ((1, u'Matutino'), 
                  (2, u'Vespertino'),
                  (3, u'Nocturno'))

class Frecuencia(models.Model):
    nombre = models.CharField(max_length=300)
    cantidad = models.IntegerField(verbose_name = u'Cantidad de dias')

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = u'Frencuencias'

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    frecuencia = models.ForeignKey(Frecuencia)
    horario = models.IntegerField(choices=CHOICE_HORARIO)

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    submodulo = models.ForeignKey(SubModulo, verbose_name = u'Area')

    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.nombre, self.fecha_inicio.strftime("%d/%m/%Y"), self.frecuencia, self.get_horario_display())

    class Meta:
        verbose_name_plural = u'Cursos'