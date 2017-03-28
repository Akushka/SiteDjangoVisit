# -*- coding: utf-8 -*
from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from siteVisit.models import SiteName, CommentArticle
from django.utils import timezone
import os.path
from django.core.context_processors import csrf
from .forms import CommentForm, NewArticleForm, EditArticleForm, FindArtikleForm, Feedback
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
    

def article_list(request, pk):
    articles = SiteName.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    
    filter = ''
    pkCat = int(pk)
    
    category = {
    0 : '',
    1 : 'Телефоны',
    2 : 'Планшеты',
    3 : 'Миникомпьютеры',
    4 : 'Игровые консоли',
    5 : 'Игрушки',
    6 : 'Детские товары',
    7 : 'Разное прикольное',
    8 : 'Запас',
    9 : 'Запас',
    10 : 'Запас'
    }
    filter = category[pkCat]
    
    for article in articles:
        article.tryCategory = False
        if article.category.lower().find(filter.lower()) > -1:
            article.tryCategory = True
        #article.save()
    
    articles.imagePath = []
    find_form = FindArtikleForm
    args = {}
    args['article'] = []
    args['form'] = find_form
    form = FindArtikleForm(request.POST)
#Если ставим фильтр    
    if request.method == "POST":
        if form.is_valid():
            findFilter = form.save(commit = False)
            for article in articles:
                article.articleFindText = findFilter.articleFindText
        
    for article in articles:
        
        article.imagePathBegin = 'media/'+article.articleTitle+'_0'+'.jpg'
        article.articleTextPreview = article.articleText[:100]
        if (article.articleText.lower().find(article.articleFindText.lower())>-1) & (article.tryCategory == True):
            args['article'].append(article)
    return render(request, 'siteVisit/Article_list.html', {'form': args['form'], 'articles' : args['article'] })

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
    STATIC_ROOT = os.path.abspath(os.path.dirname(__file__))
    for i in range(10):
        if os.path.isfile('siteVisit/static/media/'+args['article'].articleTitle+'_'+str(i)+'.jpg'):
            args['article'].imagePath.append('media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')
        #if os.path.isfile(os.path.join(STATIC_ROOT,'../static/media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')):
        #args['article'].imagePath.append(os.path.join(STATIC_ROOT+'\\static\\media\\'+args['article'].articleTitle+'_'+str(i)+'.jpg'))            
    args['article'].imagePathBegin = 'media/'+args['article'].articleTitle+'_'+str(nomImage)+'.jpg'        
    return render_to_response('siteVisit/Article_detail.html', args )


def addcomment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.article_id = SiteName.objects.get(pk=pk)
            form.save()
    return redirect('/siteVisit/sitename/%s/' % pk)        


def delComment(request, pkCom):
    if request.method == "POST":
        comment = CommentArticle.objects.get(pk=pkCom)
        pkArt = comment.article_id.id
        comment.delete()
    return redirect('/siteVisit/sitename/%s/' % pkArt)        
      
def article_add(request):
    if request.POST:
        form = NewArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_date = timezone.now()
            article.save()
            return article_list(request)
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
            #return render(request,'siteVisit/Article_detail.html', {'article': article})
            return article_detail(request, pk)
    else:
        form = EditArticleForm(instance=article)
    return render(request, 'siteVisit/article_edit.html', {'form': form})

def feedback(request):
    if request.POST:
        form = Feedback(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            textFeedback = form.cleaned_data['textFeedback']
            recepients = ['anatoliy.kushka@tns-ua.com','mysiteadmkushka@gmail.com']
            try:
                send_mail('', textFeedback, 'mysiteadmkushka@gmail.com', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            return article_list(request)
    else:
        form = Feedback()
    return render(request, 'siteVisit/FeedBack.html', {'form': form})
    
    
    
def view_left_list(request, pk):
    filter = ''
    if pk == 1:
        filter = 'Телефоны'  
    if pk == 2:
        filter = 'Планшеты'    
    if pk == 3:
        filter = 'Детские товары'
    if pk == 4:
        filter = 'Разное прикольное'
    articles = SiteName.objects.all()
    for article in articles:
        article.tryCategory = False
        if article.category.lower().find(filter.lower()) > -1:
            article.tryCategory = filter
        article.save()
    return article_list(request, pk)

   
    

    