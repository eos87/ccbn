# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

# from django.http import HttpResponseRedirect
# from django.contrib.contenttypes.generic import generic_inlineformset_factory


# def testing(request):
#     name = request.GET.get('name', 'Helmy')
#     AutorFormSet = generic_inlineformset_factory(Libro, extra=1)
#     autor = Autor.objects.get(nombre=name)
#     formset = AutorFormSet(instance=autor)
    
#     if request.method == 'POST':
#         formset = AutorFormSet(instance=autor, data=request.POST)
#         if formset.is_valid():            
#             formset.save()
#             return HttpResponseRedirect('/')            

#     return render_to_response('index.html', RequestContext(request, locals()))