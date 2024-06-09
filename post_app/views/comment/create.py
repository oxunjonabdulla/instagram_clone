from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from post_app.serializers.comment import CommentSerializer


class PostCommentCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        serializer.save(author=self.request.user,
                        post_id=post_id)
