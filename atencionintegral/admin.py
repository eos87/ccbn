from django.contrib import admin
from registro.models import (RegistroBecaPrimaria, RegistroBecaSecundaria, 
                             RegistroBecaUniversitaria)
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
               'solidario_centro','solidario_comunidad', 'solidario_sociedad')
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

# class EventoColectivaAtencionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['lugar',('fecha', 'actividad'),]}),
#         ('Participantes', {'fields': [('participantes','ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
#         ('Otros datos', {'fields': [('sensibilizacion', 'apropiacion'),'foto', 'comentarios', 'acuerdos']})
#     ]
#     class Meta:
#         js = ('js/tiny_mce/tiny_mce.js',
#               'js/basic_config.js',)

admin.site.register(BecaUniversitaria, BecaUniversitariaAdmin)
# admin.site.register(EventoColectivo, EventoColectivaAtencionAdmin)
admin.site.register(ActividadEvento)