from rest_framework.pagination import PageNumberPagination


class LargeResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get('nopage'):
            return None  # Do not paginate
        return super().paginate_queryset(queryset, request, view)


class StandardResultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get('nopage'):
            return None  # Do not paginate
        return super().paginate_queryset(queryset, request, view)
