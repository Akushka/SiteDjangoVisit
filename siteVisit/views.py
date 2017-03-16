# -*- coding: utf-8 -*
from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from siteVisit.models import SiteName, CommentArticle
from django.utils import timezone
import os.path
from django.core.context_processors import csrf
from .forms import CommentForm, NewArticleForm, EditArticleForm
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def article_list(request):
    articles = SiteName.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    articles.imagePath = []
    for article in articles:
        article.imagePathBegin = 'media/'+article.articleTitle+'_0'+'.jpg'
        article.articleTextPreview = article.articleText[:100] 
    return render(request, 'siteVisit/Article_list.html', {'articles': articles})

def article_list_(request):
    return render_to_response('siteVisit/Article_list.html', {'articles': SiteName.objects.all()})

def test(request):
    return render_to_response('siteVisit/test.html')

def article_detail(request, pk):
    #article = get_object_or_404(SiteName, pk=pk)
    #article = SiteName.object.get(pk=pk)
    #comments = CommentArticle.objects.filter(article_id = pk)
    nomImage = 0
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = SiteName.objects.get(id=pk)
    args['comments'] = CommentArticle.objects.filter(article_id = pk)
    args['form'] = comment_form
    args['article'].imagePath = []
    for i in range(10):
        if os.path.isfile('siteVisit/static/media/'+args['article'].articleTitle+'_'+str(i)+'.jpg'):
            args['article'].imagePath.append('media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')
    args['article'].imagePathBegin = 'media/'+args['article'].articleTitle+'_'+str(nomImage)+'.jpg'        
    return render_to_response('siteVisit/Article_detail.html', args )


def addcomment(request, pk):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.article_id = SiteName.objects.get(pk=pk)
            form.save()
    return redirect('/siteVisit/sitename/%s/' % pk)        
    
    
def article_add(request):
    if request.POST:
        form = NewArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.created_date = timezone.now()
            article.save()
            #return redirect('blog.views.post_detail', pk=post.pk)
            return render(request,'siteVisit/Article_list.html', {'article': article})
    else:
        form = NewArticleForm()
    return render(request, 'siteVisit/Article_new.html', {'form': form})
    
def article_edit(request, pk):
    article = get_object_or_404(SiteName, pk=pk)
    if request.method == "POST":
        form = EditArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return render(request,'siteVisit/Article_detail.html', {'article': article})
    else:
        form = EditArticleForm(instance=article)
    return render(request, 'siteVisit/article_edit.html', {'form': form, 'article': article})
    
    
    
    