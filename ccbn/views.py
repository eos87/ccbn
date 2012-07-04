# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import get_model
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from sistema.models import Salida, Modulo
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

def parse_filters(qs):
    dicc = {}
    for filtro in qs:
        if filtro.criteria:
            key = '%s%s' % (filtro.field, filtro.criteria)
        else:
            key = filtro.field

        dicc[key] = filtro.value
    
    return dicc

def salidas_list(request):
    modulos = Modulo.objects.all()
    return render_to_response('sel_programa.html', RequestContext(request, locals()))

def salida_detail(request, id=None):
    if id:
        salida = get_object_or_404(Salida, id=id)
        app_label, model = salida.model.split(',')
        model = get_model(app_label, model)
        base = model.objects
        filters_qs = salida.filter_set.all()

        if filters_qs:
            query = base.filter(**parse_filters(filters_qs))
        else:
            query = base

        if salida.tipo_meta == 1: # percent
            total = base.count()
            cantidad = query.count()
            result = get_porcentaje(total, cantidad)
        elif salida.tipo_meta == 2: # count
            result = query.count()

        # verificando splits y obteniendo valores
        splits_dicc = {}
        for split in salida.querysplit_set.all():
            sub_qs = query.filter(**{split.field:split.value})
            if split.tipo_meta == 1: # percent                
                splits_dicc[split.id] = get_porcentaje(query.count(), sub_qs.count())
            elif split.tipo_meta == 2: # count
                splits_dicc[split.id] = sub_qs.count()

    return render_to_response('salida_detail.html', RequestContext(request, locals()))
