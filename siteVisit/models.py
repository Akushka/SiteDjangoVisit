# -*- coding: utf-8 -*
from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class SiteName(models.Model):
    class Meta():
        db_table = 'siteName'
    author = models.ForeignKey('auth.User')
    articleTitle = models.CharField(max_length=200)
    articleText = models.TextField()    
    articleTextPreview = models.TextField(max_length=50)
    created_date = models.DateTimeField(
            default=timezone.now)
    imagePath = []
    imagePathBegin = models.TextField()
    def publish(self):
        self.created_date = timezone.now()
        self.save()
    def __str__(self):
        return self.articleTitle


class CommentArticle(models.Model):
    class Meta():
        db_table = 'commentArticle'
    article_id = models.ForeignKey(SiteName)
    articleAuthor = models.TextField(verbose_name = "Автор")    
    articleComment = models.TextField(verbose_name = "Текст комментария")    
    def __str__(self):
        return self.articleAuthor
    def publishCommen(self):
        self.save()

class Feedback(models.Model):
    feedbackAuthor =  models.TextField(max_length=50)
    feedbackEmail = models.TextField(max_length=50)
    feedbackComment = models.TextField()    
    def __str__(self):
        return self.feedbackAuthor
    def publishFeedback(self):
        self.save()

