#!/usr/bin/python
#-*- coding: utf-8 -*-

from time import mktime


def timestamp(a_time):
    "Convert a datetime object to java timestamp"
    return int(mktime(a_time.utctimetuple()) * 1000)

def test():
    print "Test"