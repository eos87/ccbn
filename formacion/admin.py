# -*- coding: utf-8 -*-
from django.contrib import admin
from registro.models import InscripcionCurso
from models import *

admin.site.register(Frecuencia)

class InscripcionCursoInline(admin.TabularInline):
    verbose_name_plural = u'Personas inscritas en el curso'
    model = InscripcionCurso
    max_num = 0
    extra = 0
    readonly_fields = ['persona', 'fecha']
    fields = ['persona', 'fecha', 'becado', 'estado', 'xq_no_termino', 'calificacion', 'mejora_autoestima', 'mejora_vida',
                'calidad_contenido', 'metodologia']

    class Media:
        css = {
            'screen': ('/files/css/admin.css', ),
        }


class CursoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha_inicio'
    fields = ['nombre', ('frecuencia', 'horario'), ('fecha_inicio', 'fecha_fin'), 'submodulo']
    list_display = ['nombre', 'submodulo', 'frecuencia', 'horario', 'fecha_inicio', 'fecha_fin']
    inlines = [InscripcionCursoInline, ]

class EventoColectivaFormacionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('titulo','lugar'),('fecha', 'actividad'),]}),
        ('Participantes', {'fields': [('participantes','ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': [('sensibilizacion', 'apropiacion'),'foto', 'comentarios', 'acuerdos']})
    ]
    class Media:
        js = ['js/tiny_mce/tiny_mce.js',
              'js/basic_config.js',]

admin.site.register(Curso, CursoAdmin)
admin.site.register(ActividadEvento)
admin.site.register(EventoColectivo, EventoColectivaFormacionAdmin)