#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from ringtone.services.views import retrieve_categories, retrieve_ringtones, search_ringtones, upload_ringtones

urlpatterns = patterns('',
    url(r'^categories/$', retrieve_categories),
    url(r'^ringtones/$', retrieve_ringtones),
    url(r'^ringtones/search/$', search_ringtones),
    url(r'^ringtones/upload/$', upload_ringtones),
)
