#!/usr/bin/python
#-*- coding: utf-8 -*-

import urllib

def test():
    url_opener = urllib.FancyURLopener()
    url_opener.addheader('X_RINGTONEDAY', '110718')
    url_opener.addheader('X_RTAUTHORIZATION', '4b80d3d6a072401f283ef5eb6321f451')
    print url_opener.open('http://127.0.0.1:8000/service/categories/').read()

if __name__ == '__main__':
    test()
