# -*- coding: utf-8 -*

_autor_ ='macpro'

from django.forms import ModelForm
from .models import CommentArticle, SiteName

class CommentForm(ModelForm):
    class Meta:
        model = CommentArticle
        fields = "__all__" 
        fields = ['articleAuthor','articleComment']
        
class NewArticleForm(ModelForm):
    class Meta:
        model = SiteName
        fields = ['author','articleTitle','articleText']

class EditArticleForm(ModelForm):
    class Meta:
        model = SiteName
        fields = "__all__" 
        fields = ['articleTitle','articleText']
                