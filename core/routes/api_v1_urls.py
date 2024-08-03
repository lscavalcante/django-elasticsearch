from rest_framework import routers
from django.urls import path, include

from apps.comment.views import CommentSearchViewSet
from apps.post.views import PostSearchViewSet

router = routers.DefaultRouter()
# router.register(r"authentication", AuthenticationAPI, basename='authentication')
router.register(r'posts', PostSearchViewSet, basename='postdocument')
router.register(r'comments', CommentSearchViewSet, basename='commentdocument')

urlpatterns = [
    path("", include(router.urls)),
]
