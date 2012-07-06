# -*- coding: utf-8 -*-
from django import template
from ccbn.views import parse_salida
register = template.Library()

@register.filter
def get_value(dicc, key):   
    '''donde dicc es el diccionario con valores y key la llave a obtener'''
    return dicc[key] 

@register.inclusion_tag('salida_detail_.html')
def render_salida(salida_obj):
	return parse_salida(salida_obj)