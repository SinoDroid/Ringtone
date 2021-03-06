#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^services/', include('ringtone.services.urls')),
    url(r'^mobosite/', include('ringtone.mobosite.urls')),
)
