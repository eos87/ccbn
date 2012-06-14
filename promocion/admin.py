# -*- coding: utf-8 -*-
from models import *
from django.contrib import admin
from registro.models import *

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

class MusicaInline(BasePromoArtisticaInline):
    model = RegistroMusica

class MusicaAdmin(admin.ModelAdmin):
    inlines = [MusicaInline, ]
admin.site.register(Musica, MusicaAdmin)

class TeatroInline(BasePromoArtisticaInline):
    model = RegistroTeatro

class TeatroAdmin(admin.ModelAdmin):
    inlines = [TeatroInline, ]
admin.site.register(Teatro, TeatroAdmin)

class CoroInline(BasePromoArtisticaInline):
    model = RegistroCoro

class CoroAdmin(admin.ModelAdmin):
    inlines = [CoroInline, ]
admin.site.register(Coro, CoroAdmin)

class DanzaInline(BasePromoArtisticaInline):
    model = RegistroDanza

class DanzaAdmin(admin.ModelAdmin):
    inlines = [DanzaInline, ]
admin.site.register(Danza, DanzaAdmin)

class PinturaInline(BasePromoArtisticaInline):
    model = RegistroPintura

class PinturaAdmin(admin.ModelAdmin):
    inlines = [PinturaInline, ]
admin.site.register(Pintura, PinturaAdmin)

# Eventos Colectivos
class EventoColectivoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('titulo','lugar'),('actividad', 'fecha'),]}),
        ('Participantes', {'fields': ['participantes', ('ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': ['sensibilizacion', 'apropiacion', 'foto', 'comentarios', 'acuerdos']})
    ]
    class Meta:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/basic_config.js',)

admin.site.register(EventoColectivo, EventoColectivoAdmin)