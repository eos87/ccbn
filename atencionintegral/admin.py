from django.contrib import admin
from registro.models import (RegistroBecaPrimaria, RegistroBecaSecundaria, 
                             RegistroBecaUniversitaria, RegistroFamiliaBecado)
from models import *

class BecadosPrimariaInline(admin.TabularInline):
    model = RegistroBecaPrimaria
    fields = ('persona', 'fecha', 'tutoria', 'rendimiento_academico', 'recibio_suplemento', 
               'recibio_atencion_psicologica', 'mejoro_habilidades', 'reconoce_capacidad', 'perc_derecho')
    readonly_fields = ['persona', 'fecha']
    extra = 0
    max_num = 0

    class Media:
        css = {
            'screen': ('/files/css/admin.css', ),
        }

class BecaPrimariaAdmin(admin.ModelAdmin):
    inlines = [BecadosPrimariaInline, ]

admin.site.register(BecaPrimaria, BecaPrimariaAdmin)

class BecadosSecundariaInline(admin.TabularInline):
    model = RegistroBecaSecundaria    
    fields = ('persona', 'fecha', 'servicio_social', 'esp_propos', 'promotor', 'solidario_famila', 
               'solidario_centro','solidario_comunidad', 'solidario_sociedad','bibliotecario')
    readonly_fields = ['persona', 'fecha']
    extra = 0
    max_num = 0

    class Media:
        css = {
            'screen': ('/files/css/admin.css', ),
        }

class BecaSecundariaAdmin(admin.ModelAdmin):
    inlines = [BecadosSecundariaInline, ]

admin.site.register(BecaSecundaria, BecaSecundariaAdmin)

class BecadosUniversitariosInline(BecadosSecundariaInline):
    model = RegistroBecaUniversitaria

class BecaUniversitariaAdmin(admin.ModelAdmin):
    inlines = [BecadosUniversitariosInline, ]

admin.site.register(BecaUniversitaria, BecaUniversitariaAdmin)

class FamiliaBecadoInline(admin.TabularInline):
    fields = ('persona', 'fecha', 'formacion_acompa', 'mejora_relacion', 'sens_derecho_edu', 'part_soya', 
               'madre_en_curso','padre_en_curso', 'hermano_en_curso')
    readonly_fields = ['persona', 'fecha']
    extra = 0
    max_num = 0
    model = RegistroFamiliaBecado

    class Media:
        css = {
            'screen': ('/files/css/admin.css', ),
        }

class FamiliaBecadoAdmin(admin.ModelAdmin):
    inlines = [FamiliaBecadoInline, ]

admin.site.register(FamiliaBecado, FamiliaBecadoAdmin)

class EventoColectivaAtencionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['titulo','lugar',('fecha', 'actividad'),]}),
        ('Participantes', {'fields': [('participantes','ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': [('apropiacion'),'foto', 'comentarios', 'acuerdos']})
    ]
    class Media:
        js = ['js/tiny_mce/tiny_mce.js',
              'js/basic_config.js',]

admin.site.register(EventoColectivoAtencion, EventoColectivaAtencionAdmin)
admin.site.register(ActividadEventoAtencion)