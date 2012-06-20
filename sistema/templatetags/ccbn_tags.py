# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.filter
def get_value(dicc, key):   
    '''donde dicc es el diccionario con valores y key la llave a obtener'''
    return dicc[key] 