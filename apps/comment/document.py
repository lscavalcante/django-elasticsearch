# documents.py
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Comment, Post

@registry.register_document
class CommentDocument(Document):
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(),
        'email': fields.TextField(),
    })
    post = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'author': fields.ObjectField(properties={
            'username': fields.TextField(),
            'email': fields.TextField(),
        }),
    })

    class Index:
        name = 'comments'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Comment
        fields = [
            'id',
            'text',
            'created_date',
        ]

    def prepare_author(self, instance):
        return {
            'id': instance.author.id,
            'username': instance.author.username,
            'email': instance.author.email,
        }

    def prepare_post(self, instance):
        return {
            'id': instance.post.id,
            'title': instance.post.title,
            'author': {
                'username': instance.post.author.username,
                'email': instance.post.author.email,
            },
        }
