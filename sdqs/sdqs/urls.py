from django.conf.urls import patterns, include, url
from delay_queue.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#from django.http import HttpResponse

#def hello(request):
#    return HttpResponse('hello world')

import os 
site_image = os.path.join( 
    os.path.dirname(__file__), '../delay_queue/templates/image/' 
)
site_js = os.path.join(
    os.path.dirname(__file__), '../delay_queue/templates/js/'
)


urlpatterns = patterns('',
    ('^$', index),
    ('^show_message$', show_message),
    ('^message$', handle_message),
    #('^get_message/$', get_message),
    # Examples:
    # url(r'^$', 'sdqs.views.home', name='home'),
    # url(r'^sdqs/', include('sdqs.foo.urls')),

    # media dir
    (r'^image/(?P<path>.*)$','django.views.static.serve', {'document_root': site_image}), 
    (r'^js/(?P<path>.*)$','django.views.static.serve', {'document_root': site_js}), 

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
