# -*- coding: utf-8 -*
from django.contrib import admin
from siteVisit.models import SiteName, imageInArticle
from django import forms
from .widgets import *
from django.contrib.admin.widgets import AdminFileWidget


class ImageInArticle(admin.TabularInline):
    model = imageInArticle
   # list_display = ['imagePath', 'image_img']
    readonly_fields = ['image_img']
   # fields = ['imagePath', 'image_img']
    widgets = {'image':MultiFileInput}
    extra = 1    
    
class SiteAdmin(admin.ModelAdmin):
    fields = ('author', 'articleTitle','articleText','category','tryCategory')
    inlines = [ImageInArticle]

  
        
admin.site.register(SiteName, SiteAdmin)


