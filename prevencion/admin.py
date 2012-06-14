from django.contrib import admin
from models import *

class EventoInternoAdmin(admin.ModelAdmin):
    list_display = ['actividad', 'fecha', 'lugar']
    fieldsets = [
        (None, {'fields': ['titulo','lugar', 'actividad', 'fecha',]}),
        ('Participantes', {'fields': ['participantes', ('ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': [('tematica','metodologia','apropiacion','aprendizaje','participacion'), 'foto', 'comentarios', 'acuerdos']})
    ]
    # fields = ['actividad', 'fecha','titulo','lugar', ('participantes', 'tematica'), ('metodologia',
    #             'apropiacion'), ('aprendizaje', 'participacion'), 'foto', 'comentarios', 'acuerdos']
    class Media:
        js = ['js/tiny_mce/tiny_mce.js',
            'js/basic_config.js',]

admin.site.register(EventoInterno, EventoInternoAdmin)

class EventoExternoAdmin(admin.ModelAdmin):
    list_display = ['actividad', 'fecha', 'lugar']
    filter_horizontal = ['personas', ]
    fieldsets = [
        (None, {'fields': ['titulo','lugar', 'actividad', 'fecha',]}),
        ('Participantes', {'fields': ['facilitadores', ('ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': ['tematica', 'foto', 'comentarios', 'acuerdos']})
    ]
    class Media:
        js = ['js/tiny_mce/tiny_mce.js',
            'js/basic_config.js',]


admin.site.register(EventoExterno, EventoExternoAdmin)