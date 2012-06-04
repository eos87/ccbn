# -*- coding: utf-8 -*-
from ccbn import settings
from django.db import models
import datetime

def generate_years_choice(start_year):
    actual_year = datetime.date.today().year
    return [(year, str(year)) for year in range(start_year, actual_year+1)]

EXCLUDE_APPS = (
    'auth',
    'contenttypes',
    'sessions',
    'sites',
    'messages',
    'staticfiles',
    'admin',
    'autocomplete',
    'south',
    'lugar'
)

def read_all_models():
    lista = []
    exclude = []
    for model in models.get_models():
        if not model._meta.app_label in EXCLUDE_APPS:
            if model._meta.app_label not in exclude:
                lista.append(model)
        else:
            exclude.append(model)
    return lista