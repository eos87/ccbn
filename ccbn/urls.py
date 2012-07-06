from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^index2/', 'ccbn.views.testing', name='salidasa_list'),
    url(r'^i/(?P<id>\d+)/$', 'ccbn.views.salida_detail', name='salida_detail'),
    url(r'^loadfields/$', 'ccbn.views.loadfields', name='loadfields'),
    url(r'^getfilters/$', 'sistema.views.get_filters', name='getfilters'),
    url(r'^getprestamodata/$', 'sistema.views.get_prestamo_data', name='get_prestamo_data'),

    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'index.html'}),
    url(r'^programas/$', 'ccbn.views.salidas_list', name='salidas_list'),    
    url(r'^programas/indicadores/$', 'django.contrib.auth.views.login', {'template_name': 'indicadores.html'}),
    url(r'^programas/indicadores/(?P<id>\d+)/$', 'ccbn.views.estrategia_detail', name='estrategia_detail'),    
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()