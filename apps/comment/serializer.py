from rest_framework import serializers

from apps.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_date']
