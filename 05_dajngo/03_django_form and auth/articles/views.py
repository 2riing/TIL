from django.shortcuts import get_object_or_404, redirect, render
# dvd h 로 외우면 됨
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods, require_GET
from .models import Article
from .forms import ArticleForm

# Class Based View => Declarative(선언형)
# (django에만 있음)
# 코드가 4줄이면 CRUD완성..

# Function Based View => Imperative(명령형)
@require_http_methods(['GET', 'POST'])
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): # <= 실패시 form 에 에러메시지가 담김
            article = form.save()
            return redirect('articles:detail', article.pk)
    elif request.method == 'GET':
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/form.html', context)

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

@require_safe
@login_required
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context ={
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
@require_http_methods(['GET', 'POST'])
@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid(): # <= 실패시 form 에 에러메시지가 담김
            article = form.save()
            return redirect('articles:detail', article.pk)
    elif request.method == 'GET':
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
    }
    return render(request, 'articles/form.html', context)

# 아래 함수는 POST 요청만 받음
@require_POST
@login_required
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')
