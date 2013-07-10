from django.conf.urls import patterns, include, url
from delay_queue.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#from django.http import HttpResponse

#def hello(request):
#    return HttpResponse('hello world')

urlpatterns = patterns('',
    ('^$', index),
    ('^message$', handle_message),
    #('^get_message/$', get_message),
    # Examples:
    # url(r'^$', 'sdqs.views.home', name='home'),
    # url(r'^sdqs/', include('sdqs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
