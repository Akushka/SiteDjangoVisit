# -*- coding: utf-8 -*
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.db.models.fields.files import ImageField, ImageFieldFile, FileField
from pip import *
# Create your models here.


class SiteName(models.Model):
    class Meta():
        db_table = 'siteName'
    author = models.ForeignKey('auth.User', null=True, blank=True)
    category = models.CharField(max_length=20)
    tryCategory = models.BooleanField()
    articleTitle = models.CharField(max_length=200)
    articleText = models.TextField()    
    articleTextPreview = models.TextField(max_length=50)
    articleFindText = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    imagePath = []
    imagePathBegin = models.TextField()
    #image = ImageField(upload_to='images/', null=True, blank=True)
    def publish(self):
        self.created_date = timezone.now()
        self.save()
    def __str__(self):
        return self.articleTitle
    
class imageInArticle (models.Model):
    image_id = models.ForeignKey(SiteName)
    imagePath = models.ImageField(upload_to = 'image', blank=True, null=True)
    def image_img(self):
        if self.imagePath:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.imagePath.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
 
class AutentificationUser(models.Model):
    userName = models.CharField(max_length=20,verbose_name = "User")
    passw = models.CharField(max_length=20,verbose_name = "Pass")
        
    
class CommentArticle(models.Model):
    class Meta():
        db_table = 'commentArticle'
    article_id = models.ForeignKey(SiteName)
    articleAuthor = models.CharField(max_length=200,verbose_name = "Автор")    
    articleComment = models.TextField(verbose_name = "Текст комментария")    
    def __str__(self):
        return self.articleAuthor
    def publishCommen(self):
        self.save()

