# views.py
from rest_framework import viewsets

from shared.pagination.pagination import StandardResultPagination
from .document import CommentDocument
from .models import Comment
from .serializer import CommentSerializer


class CommentSearchViewSet(viewsets.ViewSet):
    pagination_class = StandardResultPagination

    def list(self, request):
        query = request.query_params.get('q', None)
        page = request.query_params.get('page', 1)

        search = CommentDocument.search()
        if query:
            search = search.query("multi_match", query=query, fields=["author", "text", "post.title", "post.author"])

        paginator = self.pagination_class()
        paginated_search = paginator.paginate_queryset(search, request, view=self)
        results = [hit.to_dict() for hit in paginated_search]

        comments = Comment.objects.filter(id__in=[result['id'] for result in results])
        serializer = CommentSerializer(comments, many=True)
        return paginator.get_paginated_response(serializer.data)
