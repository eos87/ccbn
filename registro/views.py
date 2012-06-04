# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import get_model
from django.template import RequestContext
from sistema.models import Salida
from models import *

def testing(request):
    id = request.GET.get('id', 1)
    salida = Salida.objects.get(id=id)
    app_label, model = salida.model.split(',')
    model = get_model(app_label, model)
    query = model.objects.all()

    if salida.tipo_meta == 1: # percent
        pass
    elif salida.tipo_meta == 2: # count
        tipo_meta = query.count()

    return render_to_response('index.html', RequestContext(request, locals()))