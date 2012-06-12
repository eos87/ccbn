from django.contrib import admin
from django.core import validators
from django.core.exceptions import ValidationError
from models import *
from django import forms

class SubModuloAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'parent_module', 'inline']
    list_filter = ['parent_module']
    search_fields = ['nombre', 'parent_module__nombre']

admin.site.register(SubModulo, SubModuloAdmin)

class SubModuloInline(admin.StackedInline):
    extra = 1
    model = SubModulo

    def formfield_for_choice_field(self, db_field, request=None, **kwargs):
        if db_field.name == 'inline':
            kwargs['choices'] = (('', '---------'), ('1', 'concha'), ('2', 'uta madre'))

        return db_field.formfield(**kwargs)

class ModuloAdmin(admin.ModelAdmin):
    # inlines = [SubModuloInline, ]
    pass

admin.site.register(Modulo, ModuloAdmin)

class CustomChoiceField(forms.ChoiceField):
    def validate(self, value):
        if value in validators.EMPTY_VALUES and self.required:                                                              
            raise ValidationError(self.error_messages['required'])

class FilterForm(forms.ModelForm):
    field = CustomChoiceField(choices=(('', '---------'), ), label='Field')

class FilterInline(admin.TabularInline):
    model = Filter
    extra = 1
    form = FilterForm

    class Media:
        js= ['http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js', 
            '/files/js/query.filters.js']

class SalidaAdmin(admin.ModelAdmin):
    inlines = [FilterInline, ]

admin.site.register(Salida, SalidaAdmin)