from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from post_app.models import PostComment
from post_app.serializers.comment import CommentSerializer


class PostCommentRetrieveAPIView(RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = PostComment.objects.all()
    permission_classes = [AllowAny, ]



