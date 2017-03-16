# -*- coding: utf-8 -*
from django.conf.urls import url
from . import views
from django.conf.urls import * 
from django.contrib import *

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^siteVisit/sitename/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^siteVisit/sitename/edit/(?P<pk>[0-9]+)/$', views.article_edit, name='article_edit'),
    url(r'^siteVisit/addcomment/(?P<pk>[0-9]+)/$', views.addcomment, name='addcomment'),
    url(r'^siteVisit/article_add/$', views.article_add, name='article_add'),
    url(r'^siteVisit/sitename/test/$', views.test, name='test'),
]
