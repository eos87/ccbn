from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'registro.views.testing', name='home'),
    url(r'^loadfields/$', 'ccbn.views.loadfields', name='loadfields'),
    # url(r'^ccbn/', include('ccbn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'django.contrib.auth.views.login', {'template_name': 'index.html'}),
	#url(r'^$',direct_to_template,{'template': 'index.html'}),
    url(r'^admin/', include(admin.site.urls)),

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()