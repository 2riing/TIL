from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .models import Article

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
        # 'articles_pk' : int:article_pk,

    }
    return render(request, 'practice/article_list.html', context)

def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'practice/article_detail.html', context)