# -*- coding: utf-8 -*
from django.contrib import admin
from siteVisit.models import SiteName

    
class SiteAdmin(admin.ModelAdmin):
    fields = ('author', 'articleTitle','articleText','category','tryCategory')
    
admin.site.register(SiteName, SiteAdmin)


