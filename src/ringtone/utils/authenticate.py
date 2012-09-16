#!/usr/bin/python
#-*- coding: utf-8 -*-

from functools import wraps
import hashlib

from django.http import HttpResponse

def authentication(method):
    @wraps(method)
    def wrapper(request, *args, **kwargs):
        #Disabled authorization if debug mode is on
        if request.META.has_key('HTTP_X_RTAUTHORIZATION') and request.META.has_key('HTTP_X_RINGTONEDAY'):
            value = request.META['HTTP_X_RTAUTHORIZATION']
            date = request.META['HTTP_X_RINGTONEDAY']
            string = 'Ringtone' + date
            m5 = hashlib.md5()
            m5.update(string)
            calculated_value = m5.hexdigest().lower()
            if value == calculated_value:
                return method(request, *args, **kwargs)
        else:
            error_401 = HttpResponse()
            error_401.status_code = 401
            error_401.write("401")
            return error_401
    return wrapper
