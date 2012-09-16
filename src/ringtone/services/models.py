#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length = 50)
    icon_url = models.CharField(max_length = 200)
    content_level = models.IntegerField()
    last_modify = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'Categories'
        
        
class Ringtone(models.Model):
    name = models.CharField(max_length = 100)
    mime_type = models.CharField(max_length = 50)
    file_size = models.IntegerField()
    duration = models.IntegerField()
    url = models.CharField(max_length = 200)
    last_modify = models.DateTimeField(auto_now = True)
    view_count = models.IntegerField(default = 0)
    preview_count = models.IntegerField(default = 0)
    download_count = models.IntegerField(default = 0)
    set_as_count = models.IntegerField(default = 0)
    category = models.ForeignKey(Category)
    upload_user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name',]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_level', 'last_modify', 'icon_url')
    list_filter = ('content_level',)
    search_fields = ('name',)
    
    
class RingtoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'file_size', 'last_modify', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ringtone, RingtoneAdmin)
