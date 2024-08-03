# documents.py
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Post


@registry.register_document
class PostDocument(Document):
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(),
        'email': fields.TextField(),
    })
    comments = fields.NestedField(properties={
        'author': fields.ObjectField(properties={
            'id': fields.IntegerField(),
            'username': fields.TextField(),
            'email': fields.TextField(),
        }),
        'id': fields.IntegerField(),
        'text': fields.TextField(),
        'created_date': fields.DateField(),
    })

    class Index:
        name = 'posts'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Post
        fields = [
            'id',
            'code',  # Adicionando o campo code aqui
            'title',
            'body',
            'published_date',
        ]

    def prepare_author(self, instance):
        return {
            'id': instance.author.id,
            'username': instance.author.username,
            'email': instance.author.email,
        }

    def prepare_comments(self, instance):
        return [
            {
                'author': {
                    'id': comment.author.id,
                    'username': comment.author.username,
                    'email': comment.author.email,
                },
                'id': comment.id,
                'text': comment.text,
                'created_date': comment.created_date,
            }
            for comment in instance.comments.all()
        ]
