# serializers.py 데이터 검증, Json 생성, 1model <-> n serializer


from asyncore import read
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Article, Comment



class ArticleSerializer(serializers.ModelSerializer):

    class CommentListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            fields = ('id', 'content',) 
    # 커스텀 필드들은 read_only = True / write_only=Ture를 직접 써야함
    title = serializers.CharField(min_length=2, max_length=10)
    content = serializers.CharField(min_length=2)
    comments = CommentListSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'comments', 'created_at', 'updated_at')

class ArticleListSerializer(serializers.ModelSerializer):

    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','content', 'article',)
        read_only_fields = ('article',)


