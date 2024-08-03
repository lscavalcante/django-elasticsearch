# views.py
from django_elasticsearch_dsl.registries import registry
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from elasticsearch_dsl import Q
from faker import Faker

from apps.post.document import PostDocument
from apps.post.models import Post
from apps.post.serializer import PostSerializer, PostInput
from shared.pagination.pagination import StandardResultPagination


class PostSearchViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            search_fields = ["title", "body", "comments.text", "author.username", "author.email"]

            try:
                query_as_int = int(query)
                search = PostDocument.search().query(
                    Q("term", id=query_as_int) | Q("term", code=query_as_int)
                )
            except ValueError:
                search = PostDocument.search().query("multi_match", query=query, fields=search_fields)

            # Ordenar pelo maior ID para o menor
            search = search.sort('-id')

            return search

        return PostDocument.search().sort('-id')

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        page = self.paginate_queryset(query)

        if page is not None:
            post_ids = [hit.meta.id for hit in page]
            posts = Post.objects.filter(id__in=post_ids)
            serializer = self.get_serializer(posts, many=True)
            return self.get_paginated_response(serializer.data)

        return Response({'error': 'Pagination not applied'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = PostInput(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_created = Post.objects.create(
            **serializer.validated_data,
            author_id=1,
        )

        # registry.update(post_created)

        PostDocument().update(post_created)

        return Response(PostSerializer(instance=post_created).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Reindexar no Elasticsearch e forçar refresh
        # post_doc = PostDocument(meta={'id': instance.id}, **serializer.validated_data)
        # post_doc.save(index='posts')
        # PostDocument._index.refresh()  # Forçar o refresh do índice

        return Response(serializer.data)
