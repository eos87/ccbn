# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import get_model
from django.http import HttpResponse
from django.utils import simplejson

def loadfields(request):
    param = request.GET.get('model', None)
    lista = []
    if param:
        app_label, model_name = param.split(',')
        model = get_model(app_label, model_name)
        for field in model._meta.fields:
            if field.rel:
                for fd in field.rel.to._meta.fields:
                    lista.append('%s__%s' % (field.name, fd.name))
            else:
                lista.append(field.name)

    lista = [(elem, elem) for elem in lista]

    return HttpResponse(simplejson.dumps(lista), mimetype="application/json")