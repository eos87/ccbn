# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import get_model
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from sistema.models import Salida
from ccbn.utils import get_porcentaje

def endswith(x, value):
    if x.endswith(value): 
        return x

def loadfields(request):
    param = request.GET.get('model', None)
    lista = []

    if param:
        app_label, model_name = param.split(',')
        model = get_model(app_label, model_name)
        # obtener los campos relacionados
        # en foreignkey inversas
        related_fields = filter(lambda x: x.endswith('_set'), dir(model)) 
        for x in related_fields:
            # obtener el modelo relacionado para luego obtener sus campos
            rel_model = getattr(model, x).related.model
            x = x.replace('_set', '')
            for field in rel_model._meta.fields:
                if not isinstance(field, ForeignKey):
                    # lista.append('%s__%s' % (x, field.name))
                    pass

        for field in model._meta.fields:
            # if isinstance(field, CharField):
            #     print field
            if isinstance(field, ForeignKey):
                for fd in field.rel.to._meta.fields:
                    lista.append('%s__%s' % (field.name, fd.name))
            else:
                lista.append(field.name)

    lista = [(elem, elem) for elem in lista]

    return HttpResponse(simplejson.dumps(lista), mimetype="application/json")

def parse_filters(qs, model):
    dicc = {}
    for filtro in qs:
        if filtro.criteria:
            key = '%s%s' % (filtro.field, filtro.criteria)
        else:
            key = filtro.field
        # field = model._meta.get_field_by_name(filtro.field) # obtener el campo para saber su tipo. Eg: string, int, ....
        # luego convertir el value si es necesario
        # if isinstance(field[0], IntegerField):
            # dicc[key] = int(filtro.value)

        dicc[key] = filtro.value
    
    return dicc

def salidas_list(request):
    object_list = Salida.objects.all()
    return render_to_response('index2.html', RequestContext(request, locals()))

def salida_detail(request, id=None):
    if id:
        salida = get_object_or_404(Salida, id=id)
        app_label, model = salida.model.split(',')
        model = get_model(app_label, model)
        base = model.objects
        filters_qs = salida.filter_set.all()

        if filters_qs:
            query = base.filter(** parse_filters(filters_qs, model))

        if salida.tipo_meta == 1: # percent
            total = base.count()
            cantidad = query.count()
            result = get_porcentaje(total, cantidad)
        elif salida.tipo_meta == 2: # count
            result = base.count()

    return render_to_response('salida_detail.html', RequestContext(request, locals()))
