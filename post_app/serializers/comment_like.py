from rest_framework import serializers

from post_app.models import CommentLike
from post_app.serializers.post import UserSerializer


class CommentLikeModelSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = CommentLike

    fields = [
        "id",
        "author",
        "comment"
    ]
