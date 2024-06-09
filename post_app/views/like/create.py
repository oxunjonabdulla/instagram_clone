from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from post_app.models import PostLike, CommentLike
from post_app.serializers.comment_like import CommentLikeModelSerializer
from post_app.serializers.post_like import PostLikeSerializer


class PostLikeCreateAPIView(CreateAPIView):
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        if PostLike.objects.filter(author=self.request.user, post_id=post_id).exists():
            return Response({"success": False, "message": "Already liked"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save(author=self.request.user,
                        post_id=post_id)


class CommentLikeCreateApiView(CreateAPIView):
    serializer_class = CommentLikeModelSerializer
    queryset = CommentLike.objects.all()
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        comment_id = self.kwargs['pk']
        if CommentLike.objects.filter(author=self.request.user, comment_id=comment_id).exists():
            return Response({"success": False, "message": "Already liked"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save(author=self.request.user,
                        comment_id=comment_id)
