from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    indexed = models.BooleanField(default=False)
    code = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')

    class Meta:
        ordering = ['-id']
