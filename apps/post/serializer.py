# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

from apps.comment.models import Comment
from apps.post.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_date', 'post']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'published_date', 'comments', 'code']


class PostInput(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
