# -*- coding: utf-8 -*-
from django.db import models
from ccbn.utils import generate_years_choice
import datetime

START_YEAR = 2012

class BaseBeca(models.Model):
    year = models.IntegerField('Año de beca', choices=generate_years_choice(START_YEAR))

    def __unicode__(self):
        return u'Beca del año %s' % self.year

    class Meta:
        abstract = True

class BecaPrimaria(BaseBeca):
    class Meta:
        verbose_name_plural = u'Becas de Primaria'

class BecaSecundaria(BaseBeca):
    class Meta:
        verbose_name_plural = u'Becas de Secundaria'

class BecaUniversitaria(BaseBeca):
    class Meta:
        verbose_name_plural = u'Becas Universitarias'