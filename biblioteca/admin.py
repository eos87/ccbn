from django.contrib import admin
from django import forms
from models import *

class ConsultaInline(admin.TabularInline):
    model = Consulta
    extra = 1

class PrestamoInline(admin.TabularInline):
    model = Prestamo
    extra = 1
    max_num = 1

    class Media:
        css = {
            'screen': ('/files/css/biblioteca-prestamo.css', ),
        }
        js= ['/files/js/biblioteca-prestamo.js']

class RetornoInline(admin.TabularInline):
    model = Retorno
    extra = 1
    max_num = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(RetornoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'libro':
            editable_ids = request._obj_.retorno_set.all().values_list('libro__id', flat=True)
            exclude = Libro.objects.filter(retorno__actividad__persona=request._obj_.persona)\
                        .exclude(id__in=editable_ids)\
                        .values_list('id', flat=True)
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(prestamo__actividad__persona=request._obj_.persona).exclude(id__in=exclude)
            else:
                field.queryset = field.queryset.none()
        return field

    class Media:
        css = {
            'screen': ('/files/css/biblioteca-prestamo.css', ),
        }
        js= ['/files/js/biblioteca-retorno.js']

class ServicioInline(admin.TabularInline):
    model = Servicio
    extra = 1

class ActividadIndividualAdmin(admin.ModelAdmin):
    list_display = ['display', 'fecha', 'actividad', 'libros']
    list_filter = ['fecha', 'actividad']
    search_fields = ['persona__primer_nombre','persona__segundo_nombre',
                     'persona__primer_apellido','persona__segundo_apellido']
    add_form_template = 'admin/registro/add_form_template.html'
    inlines = []

    class Media:
        css = {
            'screen': ('/files/css/admin.css', '/files/js/chosen.css'),
        }
        js= ['http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js', 
            '/files/js/chosen.jquery.min.js', '/files/js/admin.js', '/files/js/biblioteca.js']

    def add_view(self, request):
        self.inlines=[]
        return super(ActividadIndividualAdmin, self).add_view(request)

    def change_view(self, request, obj_id):
        self.inlines = []
        inlines = []  
        try:
            obj = ActividadIndividual.objects.get(id=obj_id)
            self.inlines.append(eval(obj.actividad))
        except Exception as e:            
            print e

        return super(ActividadIndividualAdmin, self).change_view(request, obj_id)

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(ActividadIndividualAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(ActividadIndividual, ActividadIndividualAdmin)

class ActividadColectivaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('fecha', 'actividad'),]}),
        ('Participantes', {'fields': [('ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': ['evaluacion_rapida', 'foto', 'comentarios', 'acuerdos']})
    ]
admin.site.register(ActividadColectiva, ActividadColectivaAdmin)
admin.site.register(NombresActividades)

class LibroAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'registro', 'categoria']
    list_display = ['titulo', 'registro', 'categoria']

admin.site.register(Libro, LibroAdmin)