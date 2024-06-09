from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from post_app.models import PostComment
from post_app.serializers.comment import CommentSerializer
from shared_app.custom_pagination import CustomPagination


class PostCommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = PostComment.objects.all()
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = PostComment.objects.filter(post_id=post_id)
        return queryset


class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = PostComment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
