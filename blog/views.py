from django.shortcuts import render

from django.http import HttpResponseRedirect

from . import models


def test(request):
    articles = models.Article.objects.all()
    return render(request,'blog/demo.html',{'h':articles})


def article_page(request,article_id):
    article1 = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'h1':article1})


def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article1 = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'h1':article1})


def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id','0')
    if article_id == '0':
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/demo.html', {'h': articles})
    article1 = models.Article.objects.get(pk=article_id)
    article1.title = title
    article1.content= content
    article1.save()
    return render(request,'blog/article_page.html',{'h1':article1})