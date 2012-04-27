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

admin.site.register(Curso, CursoAdmin)