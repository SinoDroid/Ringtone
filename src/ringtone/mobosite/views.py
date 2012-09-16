#!/usr/bin/python
#-*- coding: utf-8 -*-

import logging

from django.http import HttpResponse
from django.template import loader, Context

from ringtone.services.models import Category
from ringtone.services.providers import query_ringtones

    
def category(request):
    categories = Category.objects.all()
    context_dict = {
        'categories' : categories,
        'count' : len(categories),
    }
    t = loader.get_template('category.tpl')
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def retrieve(request, category, order, page_size, page_no):
    
    category = int(category)
    page_size = int(page_size)
    page_no = int(page_no)
    
    ringtones = query_ringtones(category, None, order)
    
    page_count = (len(ringtones) + page_size - 1) / page_size
    start = page_size * (page_no - 1)
    end = start + page_size
    ringtones = ringtones[ start : end ]
    
    if page_count == 0:
        page_no = 0
        
    category_name = ' '
    if category > 0:
        category_name = Category.objects.filter(id=category)[0].name
    
    ringtone_list = []
    i = 1
    for ringtone in ringtones:
        ringtone_dict = {
            'name' : ringtone.name,
            'category' : ringtone.category.name,
            'size' : ringtone.file_size / 1000,
            'link' : '/mobosite/retrieve/' + str(category) + '/' + order + '/1/' + str(page_size * (page_no - 1) + i) + '/',
            'download_link' : ringtone.url,
        }
        ringtone_list.append(ringtone_dict)
        i = i + 1
        
    tab_title = 'Latest'
    tab_class = 'tab1'
    if order == 'recent':
        tab_title = 'Latest'
        tab_class = 'tab1'
    else:
        tab_title = 'Popular'
        tab_class = 'tab2'
        
    context_dict = {
        'ringtones' : ringtone_list,
        'category_name' : category_name,
        'category_id' : category,
        'tab_name' : tab_title,
        'tab_index' : tab_class,
        'page_no' : page_no,
        'page_count' : page_count,
        'prev_link' : '/mobosite/retrieve/' + str(category) + '/' + str(order) + '/' + str(page_size) + '/' + str(page_no - 1) + '/',
        'next_link' : '/mobosite/retrieve/' + str(category) + '/' + str(order) + '/' + str(page_size) + '/' + str(page_no + 1) + '/',
    }
    
    if page_size == 1:
        t = loader.get_template('ringtone.tpl')
    else:
        t = loader.get_template('retrieve.tpl')
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def search(request, category, order, page_size, page_no):
    
    category = int(category)
    page_size = int(page_size)
    page_no = int(page_no)
    keyword = request.GET.get('k', '')
    noresult = 'No result'
    
    if keyword == '':
        ringtones = []
        noresult = 'Please input a keyword.'
    else:
        ringtones = query_ringtones(category, keyword, order)
    
    page_count = (len(ringtones) + page_size - 1) / page_size
    start = page_size * (page_no - 1)
    end = start + page_size
    ringtones = ringtones[ start : end ]
    
    if page_count == 0:
        page_no = 0
        

    ringtone_list = []
    i = 1
    for ringtone in ringtones:
        ringtone_dict = {
            'name' : ringtone.name,
            'category' : ringtone.category.name,
            'size' : ringtone.file_size / 1000,
            'link' : '/mobosite/search/' + str(category) + '/' + order + '/1/' + str(page_size * (page_no - 1) + i) + '/?k=' + keyword,
            }
        ringtone_list.append(ringtone_dict)
        i = i + 1

        
    context_dict = {
        'ringtones' : ringtone_list,
        'keyword' : keyword,
        'noresult' : noresult,
        'page_no' : page_no,
        'page_count' : page_count,
        'prev_link' : '/mobosite/search/' + str(category) + '/' + str(order) + '/' + str(page_size) + '/' + str(page_no - 1) + '/?k=' + keyword,
        'next_link' : '/mobosite/search/' + str(category) + '/' + str(order) + '/' + str(page_size) + '/' + str(page_no + 1) + '/?k=' + keyword,
    }
    
    if page_size == 1:
        t = loader.get_template('ringtone.tpl')
    else:
        t = loader.get_template('search.tpl')
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def index(request):
    return retrieve(request, 0, 'recent', 10, 1)
