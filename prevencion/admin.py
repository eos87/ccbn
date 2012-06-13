from django.contrib import admin
from models import *

class EventoInternoAdmin(admin.ModelAdmin):
    list_display = ['actividad', 'fecha', 'lugar']
    fields = ['actividad', 'fecha','lugar', ('participantes', 'tematica'), ('metodologia',
                'apropiacion'), ('aprendizaje', 'participacion'), 'foto', 'comentarios', 'acuerdos']

admin.site.register(EventoInterno, EventoInternoAdmin)

class EventoExternoAdmin(admin.ModelAdmin):
    list_display = ['actividad', 'fecha', 'lugar']
    filter_horizontal = ['personas', ]
    fieldsets = [
        (None, {'fields': ['lugar', 'actividad', 'fecha',]}),
        ('Participantes', {'fields': ['facilitadores', ('ninos', 'ninas', 'jovenes_hombres'), 
                                                        ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres'), 'personas']}),
        ('Otros datos', {'fields': ['tematica', 'foto', 'comentarios', 'acuerdos']})
    ]

admin.site.register(EventoExterno, EventoExternoAdmin)