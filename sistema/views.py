from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from biblioteca.models import *
from models import *

def get_filters(request):
    ''' Retorna los filters para una salida_id dada'''
    id = request.GET.get('id', None)
    split = request.GET.get('split', None)
    lista = []
    if id:
        salida = get_object_or_404(Salida, id=id)
        if split:
            for split in salida.querysplit_set.all().order_by('id'):
                lista.append(dict(id=id, field=split.field))
        else:
            for filter in salida.filter_set.all().order_by('id'):
                lista.append(dict(id=id, field=filter.field))

    return HttpResponse(simplejson.dumps(lista), mimetype="application/json")

def get_prestamo_data(request):
    libro_id = request.GET.get('id', None)
    person_id = request.GET.get('person', None)
    if libro_id and person_id:
        try:
            prestamo = Prestamo.objects.get(libro__id=libro_id, actividad__persona__id=person_id)
            return HttpResponse(prestamo.fecha_retorno.strftime('%m/%d/%Y'), 
                                mimetype="application/javascript")        
        except Exception as e:
            print e
            return HttpResponse('There\'s something wrong!')        
    return HttpResponse('OK')