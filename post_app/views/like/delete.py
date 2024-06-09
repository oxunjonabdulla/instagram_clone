from rest_framework.generics import DestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from post_app.models import PostLike, CommentLike
from post_app.serializers.comment_like import CommentLikeModelSerializer
from post_app.serializers.post_like import PostLikeSerializer


class PostLikeDestroyAPIView(DestroyAPIView):
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        queryset = self.get_queryset()
        post_pk = self.kwargs['pk']
        post_like_pk = self.kwargs['post_like_pk']

        obj = get_object_or_404(queryset=queryset,
                                post_id=post_pk,
                                pk=post_like_pk)
        return obj


class CommentLikeDestroyAPIView(DestroyAPIView):
    serializer_class = CommentLikeModelSerializer
    queryset = CommentLike.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        queryset = self.get_queryset()
        comment_pk = self.kwargs['pk']
        comment_like_pk = self.kwargs['comment_like_pk']
        obj = get_object_or_404(
            queryset=queryset, comment_id=comment_pk, pk=comment_like_pk
        )
        return obj
