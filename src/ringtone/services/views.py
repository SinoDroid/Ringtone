#!/usr/bin/python
#-*- coding: utf-8 -*-

import random

from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.admin.models import User

from ringtone.services.models import Category, Ringtone
from ringtone.services.providers import query_ringtones, page_ringtones, jsonize_ringtones
from check import check_query_string
from ringtone.utils.datetime import timestamp


def retrieve_categories(request):
    'Retrieve all categories.'
    response = HttpResponse()
    if request.method == 'GET':
        categories = Category.objects.all()
        category_list = []
        for category in categories:
            category_dict = {
            'Id' : category.id,
            'Name' : category.name,
            'IconUrl' : category.icon_url,
            'ContentLevel' : category.content_level,
            'LastModify' : timestamp(category.last_modify),
            }
            category_list.append(category_dict)
        response.write(simplejson.dumps(category_list))
    else:
        response.status_code = 405
    return response


@check_query_string
def search_ringtones(request):
    'Search ringtones by a keyword.'
    query_dict = request.GET
    keyword = query_dict.get('keyword', '')
    category_id = query_dict.get('category_id', '0')
    sort_order = query_dict.get('sort_order', '')
    page_size = query_dict.get('page_size', '20')
    page_no = query_dict.get('page_no', '1')
    ringtones = query_ringtones(int(category_id), keyword, sort_order)
    ringtones = page_ringtones(ringtones, int(page_size), int(page_no))
    json = jsonize_ringtones(ringtones)
    return HttpResponse(json)


@check_query_string
def retrieve_ringtones(request):
    'Retrieve ringtones by category'
    #response["Content-Type"] = "application/json"
    query_dict = request.GET
    category_id = query_dict.get('category_id', '0')
    sort_order = query_dict.get('sort_order', '')
    page_size = query_dict.get('page_size', "20")
    page_no = query_dict.get('page_no', '1')
    ringtones = query_ringtones(int(category_id), None, sort_order)
    ringtones = page_ringtones(ringtones, int(page_size), int(page_no))
    json = jsonize_ringtones(ringtones)
    return HttpResponse(json)


def upload_ringtones(request):
    try:
        if request.method == 'GET':
            name = request.GET['Title']
            mime_type = request.GET['MimeType']
            file_size = request.GET['FileSize']
            duration = request.GET['Duration']
            url = request.GET['Url']
            category_name = request.GET['CategoryName']
            category = Category.objects.get(name=category_name)
            luck_man = random.randint(1, 10)
            luck_user = User.objects.get(id=luck_man)
            new_ringtone = Ringtone(name=name, 
                mime_type=mime_type,
                file_size=file_size,
                duration=duration,
                url=url,
                category=category,
                upload_user=luck_user)
            new_ringtone.save()
        else:
            pass
    except Exception, e:
        error_res = e.message
        return HttpResponse('New ringtone' + error_res)
    response = HttpResponse()
    response.write('True')
    return response
