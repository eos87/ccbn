# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from autocomplete.widgets import *
from models import *
from sistema.models import *

class RelacionInline(admin.TabularInline):
    model = Relacion
    fk_name = 'owner'
    extra = 1
    verbose_name_plural = u'Personas de su hogar que esten en CCBN'

class ModuloPersonaInline(admin.StackedInline):
    model = ModuloPersona
    verbose_name_plural = u'Programas a los que pertenece'
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

# Formacion Basica Inline
class FormacionBasicaInline(AutocompleteStackedInline):
    foo = True # variable para crear choices en modulos del sistema
    model = InscripcionCurso
    fields = (('curso', 'becado', 'fecha'),)
    related_search_fields = {
                    'curso': ('nombre',),
            }
    extra = 1
    verbose_name_plural = u'Educación Básica'

    def queryset(self, request):
        queryset = super(FormacionBasicaInline, self).queryset(request)\
                    .filter(curso__submodulo__code='educacionbasica')

        if not self.has_change_permission(request):
            queryset = queryset.none()
        return queryset 

# Formacion Tecnica Vocacional
class FormacionVocacionalInline(AutocompleteStackedInline):
    foo = True # variable para crear choices en modulos del sistema
    model = InscripcionCurso
    fields = (('curso', 'becado'), )
    related_search_fields = {
                    'curso': ('nombre',),
            }
    extra = 1

    verbose_name_plural = u'Formación Técnica Vocacional'

    def queryset(self, request):
        queryset = super(FormacionVocacionalInline, self).queryset(request)\
                    .filter(curso__submodulo__code='formacionvocacional')

        if not self.has_change_permission(request):
            queryset = queryset.none()
        return queryset 

class PersonaAdmin(AutocompleteModelAdmin):
    fieldsets = [
        ('Datos personales', {'fields': [('primer_nombre', 'segundo_nombre'), ('primer_apellido', 'segundo_apellido'), 
                                        ('sexo', 'fecha_nacimiento'), ('codigo', 'cedula'), ('personal_ccbn', 'docente_ccbn')]}),
        ('Ubicacion', {'fields': [('municipio', 'ciudad'), ('barrio', 'distrito'), 'direccion', ('telefono', 'celular')]}),
        (u'Información Académica', {'fields': [('nivel_academico', 'nivel_estudio'), 'centro_actual']}),
        ('Datos del Hogar', {'fields': ['oficio', 'con_quien_vive', 'tipo_familia',]}),
        ('Jefe de Familia', {'fields': [('jefe_familia', 'j_oficio'), ('j_primer_nombre', 'j_segundo_nombre'), 
                                        ('j_primer_apellido', 'j_segundo_apellido')],})
                                                                                     
    ]

    inlines = [RelacionInline, ModuloPersonaInline, FormacionBasicaInline, FormacionVocacionalInline]

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    related_search_fields = {

            }

    # def add_view(self, request):
    #     self.inlines=[]
    #     for inline_class in self.inlines:
    #         inline_instance = inline_class(self.model, self.admin_site)
    #         self.inline_instances.append(inline_instance)
    #     return super(PersonaAdmin, self).add_view(request)

    class Media:
        css = {
            'screen': ('/files/css/admin.css', ),
        }


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Pariente)
admin.site.register(Relacion)
admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Oficio)