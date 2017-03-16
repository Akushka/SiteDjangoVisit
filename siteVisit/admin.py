# -*- coding: utf-8 -*
from django.contrib import admin
from siteVisit.models import SiteName, CommentArticle

class ChoiceInline(admin.TabularInline):
    model = CommentArticle
    list_display = ('articleAuthor')
    extra = 2
    
class SiteAdmin(admin.ModelAdmin):

    list_display = ('articleTitle', 'created_date')
    inlines = [ChoiceInline]
    
    
admin.site.register(SiteName, SiteAdmin)
