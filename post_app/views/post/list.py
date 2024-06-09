from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from post_app.models import Post
from post_app.serializers.post import PostModelSerializer
from shared_app.custom_pagination import CustomPagination


class PostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Post.objects.all()
