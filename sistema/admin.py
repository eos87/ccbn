from django.contrib import admin
from models import *

class SubModuloAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'parent_module']
    list_filter = ['parent_module']
    search_fields = ['nombre', 'parent_module__nombre']

admin.site.register(SubModulo, SubModuloAdmin)

class SubModuloInline(admin.StackedInline):
    extra = 1
    model = SubModulo
    def get_form(self, request, obj=None, ** kwargs):
        print 'No pasa por aca XD'
        form = super(SubModuloInline, self).get_form(request, ** kwargs)
        form.base_fields['inline'].choices = ((1, 'concha'), (2, 'uta madre'))
        return form

    def formfield_for_choice_field(self, db_field, request=None, **kwargs):
        if db_field.name == 'inline':
            kwargs['choices'] = (('', '---------'), ('1', 'concha'), ('2', 'uta madre'))

        return db_field.formfield(**kwargs)

class ModuloAdmin(admin.ModelAdmin):
    inlines = [SubModuloInline, ]

admin.site.register(Modulo, ModuloAdmin)