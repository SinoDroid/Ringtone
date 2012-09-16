#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from ringtone.mobosite.views import category, search, retrieve, index

urlpatterns = patterns('',
    url(r'^$', index),                   
    url(r'^category$', category),
    url(r'^retrieve/(?P<category>\d+)/(?P<order>(popular)|(recent))/(?P<page_size>\d+)/(?P<page_no>\d+)/$', retrieve),
    url(r'^search/(?P<category>\d+)/(?P<order>(popular)|(recent))/(?P<page_size>\d+)/(?P<page_no>\d+)/$', search),
)
