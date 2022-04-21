

from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import (
    ArticleSerializer, ArticleListSerializer, CommentSerializer)
from articles import serializers


@api_view(['GET','POST'])
def article_index_create(request):

    def article_index():
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def article_create():
        serializer = ArticleSerializer(data=request.data) # data를 가져옴
        if serializer.is_valid(raise_exception=True): 
        # is vaild 하지 않으면 else의 역할을 함
            serializer.save()
            return Response(serializer.data) # 객체 변환

    if request.method == 'GET':
        return article_index()
    elif request.method == 'POST':
        return article_create()





@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def article_update():
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def article_delete():
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method =='GET':
        return article_detail()
    elif request.method == 'PUT':
        return article_update()
    elif request.method == 'DELETE':
        return article_delete()

# 데코레이터 필수 
@api_view(['GET','POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    def comment_create():
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data)

    return comment_create()

@api_view(['PUT','DELETE'])
def comment_update_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def comment_update():
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def comment_delete():
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    if request.method == 'PUT':
        return comment_update()
    elif request.method == 'DELETE':
        return comment_delete()    