from django.contrib import admin
from models import *

class ConsultaInline(admin.TabularInline):
    model = Consulta
    extra = 1

class PrestamoInline(admin.TabularInline):
    model = Prestamo
    extra = 1

class RetornoInline(admin.TabularInline):
    model = Retorno
    extra = 1

class ServicioInline(admin.TabularInline):
    model = Servicio
    extra = 1

class ActividadIndividualAdmin(admin.ModelAdmin):
    list_display = ['persona', 'fecha', 'actividad']
    add_form_template = 'admin/registro/add_form_template.html'
    inlines = []

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

admin.site.register(ActividadIndividual, ActividadIndividualAdmin)

class ActividadColectivaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('fecha', 'actividad'),]}),
        ('Participantes', {'fields': [('ninos', 'ninas', 'jovenes_hombres'), ('jovenes_mujeres', 'adultos_hombres', 'adultos_mujeres')]}),
        ('Otros datos', {'fields': ['evaluacion_rapida', 'foto', 'comentarios', 'acuerdos']})
    ]
admin.site.register(ActividadColectiva, ActividadColectivaAdmin)