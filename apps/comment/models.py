from django.contrib.auth.models import User
from django.db import models

from apps.post.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    indexed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
