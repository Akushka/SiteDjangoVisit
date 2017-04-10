# -*- coding: utf-8 -*
from django.conf.urls import url
from . import views
from django.conf.urls import * 
from django.contrib import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.article_list, name='article_list'),
    url(r'^siteVisit/autentificationUser/$', views.autentificationUser, name='autentificationUser'),
    url(r'^siteVisit/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^siteVisit/edit/(?P<pk>[0-9]+)/$', views.article_edit, name='article_edit'),
    url(r'^siteVisit/addcomment/(?P<pk>[0-9]+)/$', views.addcomment, name='addcomment'),
    url(r'^siteVisit/delComment/(?P<pkCom>[0-9]+)/$', views.delComment, name='delComment'),
    url(r'^siteVisit/delArticle/(?P<pk>[0-9]+)/$', views.delArticle, name='delArticle'),
    url(r'^siteVisit/delPicture/(?P<pkArt>[0-9]+)/(?P<pkPic>[0-9]+)/$', views.delPicture, name='delPicture'),
    url(r'^siteVisit/article_add/$', views.article_add, name='article_add'),
    url(r'^siteVisit/test/$', views.test, name='test'),
    url(r'^siteVisit/FeedBack/$', views.feedback, name='feedback'),
    url(r'^siteVisit/(?P<pk>[0-9]+)/$', views.view_left_list, name='view_left_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
