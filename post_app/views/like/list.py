from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from post_app.models import PostLike, CommentLike
from post_app.serializers.comment import CommentSerializer
from post_app.serializers.comment_like import CommentLikeModelSerializer
from post_app.serializers.post_like import PostLikeSerializer


class PostLikeListAPIView(ListAPIView):
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = PostLike.objects.filter(post_id=post_id)
        return queryset


class CommentLikeListAPIView(ListAPIView):
    serializer_class = CommentLikeModelSerializer
    queryset = CommentLike.objects.all()
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        comment_id = self.kwargs["pk"]
        queryset = CommentLike.objects.filter(comment_id=comment_id)
        return queryset
