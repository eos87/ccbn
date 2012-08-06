from django.contrib import admin
from models import *

class EventoInternoAdmin(admin.ModelAdmin):
    list_display = ['actividad', 'fecha', 'lugar']
    fieldsets = [
        (None, {'fields': ['titulo','lugar', 'actividad', 'fecha',]}),
        ('Participantes', {'fields': ['participantes', ('ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': [('tematica','metodologia','apropiacion','aprendizaje','participacion'), 'foto', 'comentarios', 'acuerdos']})
    ]
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
        ('Otros datos', {'fields': ['tematica', 'foto', 'comentarios', 'acuerdos','personas']})
    ]
    class Media:
        js = ['js/tiny_mce/tiny_mce.js',
            'js/basic_config.js',]

admin.site.register(EventoExterno, EventoExternoAdmin)

class PrevInternaInline(admin.TabularInline):
    model = InscripcionPrevencionInterna
    max_num = 0
    extra = 0
    readonly_fields = ['persona', 'fecha']
    fields = ['persona', 'fecha', 'asistencia', 'razon_no_asistir', 'calificacion', 'mejora_autoestima', 
               'nivel_conocimiento', 'calidad_contenido', 'metodologia', 'empoderamiento']

    class Media:
        css = {
            'screen': ('/files/css/admin.css', ),
        }

class PrevencionInternaAdmin(admin.ModelAdmin):
    inlines = [PrevInternaInline, ]

admin.site.register(PrevencionInterna, PrevencionInternaAdmin)