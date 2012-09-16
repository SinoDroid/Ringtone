#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.utils import simplejson
from django.conf import settings

from ringtone.services.models import Ringtone
from ringtone.utils.datetime import timestamp



def query_ringtones(category_id, keyword, sort_order):
    'Retrieve ringtones by category and/or keywords.'
    ringtones = Ringtone.objects.all()
    if category_id > 0:
        ringtones = ringtones.filter(category=category_id)
    if keyword:
        ringtones = ringtones.filter(name__contains=keyword)
    if sort_order in settings.SORT_ORDERS.keys():
        ringtones = ringtones.order_by(settings.SORT_ORDERS.get(sort_order))
        pass
    return ringtones


def page_ringtones(ringtones, page_size = settings.DEFAULT_PAGE_SIZE, page_no = settings.DEFAULT_PAGE_NO):
    'Page the ringtones.'
    pageinator = Paginator(ringtones, page_size)
    try:
        page = pageinator.page(int(page_no))
        object_list = page.object_list
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        object_list = []
    return object_list


def jsonize_ringtones(ringtones):
    'Convert the ringtone list to JSON array.'
    ringtone_list = []
    for ringtone in ringtones:
        ringtone_dict = {
        "Id" : ringtone.id,
        "Name" : ringtone.name,
        "MimeType" : ringtone.mime_type,
        "FileSize" : ringtone.file_size,
        "Duration" : ringtone.duration,
        "Url" : ringtone.url,
        "LastModify" : timestamp(ringtone.last_modify),
        "CategoryId" : ringtone.category.id,
        "CategoryName" : ringtone.category.name,
        "UserId" : ringtone.upload_user.id,
        }
        ringtone_list.append(ringtone_dict)
    return simplejson.dumps(ringtone_list)