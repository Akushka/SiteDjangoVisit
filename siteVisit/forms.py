# -*- coding: utf-8 -*

_autor_ ='macpro'

from django.forms import ModelForm
from .models import CommentArticle, SiteName
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = CommentArticle
        fields = "__all__" 
        fields = ['articleAuthor','articleComment']
        
class NewArticleForm(ModelForm):
    class Meta:
        model = SiteName
        fields = ['author','articleTitle','articleText','category']

class EditArticleForm(ModelForm):
    class Meta:
        model = SiteName
        fields = "__all__" 
        fields = ['articleTitle','articleText','category']
        

class FindArtikleForm(ModelForm):
    class Meta:
        model = SiteName
        fields = ['articleFindText']

class Feedback(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))  
    textFeedback = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'})) 
    fields = ['email','textFeedback']
                