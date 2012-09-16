#!/usr/bin/python
#-*- coding: utf-8 -*-

from functools import wraps

from django.http import HttpResponse

from django.conf import settings

def check_query_string(method):
    @wraps(method)
    def wrapper(request, *args, **kwargs):
        if request.method == 'GET':
            has_error = False
            error_messages = ''
            query_string_dict = request.GET
            category_id = query_string_dict.get("category_id", '0')
            sort_order = query_string_dict.get("sort_order", '')
            page_size = query_string_dict.get("page_size", '20')
            page_no = query_string_dict.get("page_no",'1')
            if not category_id.isdigit():
                has_error = True
                error_messages += "Query parameter error: category_id should be a number;"
            if sort_order != '' and not sort_order in settings.SORT_ORDERS.keys():
                has_error = True
                error_messages += "Query parameter error: no such sort order: " + sort_order
            if not page_size.isdigit() or int(page_size) <= 0:
                has_error = True
                error_messages += "Query parameter error: page_size should be positive number;"
            if not page_no.isdigit() or int(page_no) <= 0:
                has_error = True;
                error_messages += "Query parameter error: page_no should be positive number and be larger than 1;"
            if has_error:
                error_code_405 = HttpResponse()
                error_code_405.status_code = 405
                error_code_405.write(error_messages)
                return error_code_405
            return method(request, *args, **kwargs)
        else:
            error_code_403 = HttpResponse()
            error_code_403.status_code = 403
            error_code_403.write("403")
            return error_code_403
    return wrapper


def parse_query_string_error(query):
    'Parse the query strings'
    category_id = query.get("category_id", '0')
    sort_order = query.get("sort_order", '')
    page_size = query.get("page_size", '20')
    page_no = query.get("page_no",'1')
    error_messages = ''
    if not category_id.isdigit():
        error_messages += "Query parameter error: category_id should be a number;"
    if sort_order != '' and not sort_order in settings.SORT_ORDERS.keys():
        error_messages += "Query parameter error: no such sort order: " + sort_order
    if not page_size.isdigit() or int(page_size) <= 0:
        error_messages += "Query parameter error: page_size should be positive number;"
    if not page_no.isdigit() or int(page_no) <= 0:
        error_messages += "Query parameter error: page_no should be positive number and be larger than 1;"
    return error_messages