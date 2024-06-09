from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from post_app.serializers.post import PostModelSerializer


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
