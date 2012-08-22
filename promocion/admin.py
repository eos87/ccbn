# -*- coding: utf-8 -*-
from django.contrib import admin
from registro.models import *
from models import *

class BasePromoArtisticaInline(admin.TabularInline):
    fields = ['persona', 'fecha', 'asistencia', 'razon_no_continuar', 'calificacion',
            'valores_ccbn', 'genero', 'mejora_capacidad', 'utilidad_para_vida', 'calidad_creativa',
            'metodologia', 'perspectiva']
    readonly_fields = ['persona', 'fecha']

    extra = 0
    max_num = 0

    class Media:
        css = {
            'screen': ('/files/css/admin.css',),
        }

class InscripcionGrupoInline(BasePromoArtisticaInline):
    model = InscripcionGrupo

class GrupoAdmin(admin.ModelAdmin):
    inlines = [InscripcionGrupoInline]
admin.site.register(Grupo, GrupoAdmin)

# Eventos Colectivos
class EventoColectivoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('titulo','lugar'),('actividad', 'fecha'),]}),
        ('Participantes', {'fields': ['participantes', ('ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': ['sensibilizacion', 'apropiacion', 'foto', 'comentarios', 'acuerdos']})
    ]
    class Media:
        js = ['js/tiny_mce/tiny_mce.js',
              'js/basic_config.js',]

admin.site.register(EventoColectivo, EventoColectivoAdmin)