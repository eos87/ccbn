from django.contrib import admin
from models import *

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