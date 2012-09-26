#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ringtone.services.views',
    url(r'^categories/$', 'retrieve_categories'),
    url(r'^ringtones/$', 'retrieve_ringtones'),
    url(r'^ringtones/search/$', 'search_ringtones'),
    url(r'^ringtones/upload/$', 'upload_ringtones'),
)
