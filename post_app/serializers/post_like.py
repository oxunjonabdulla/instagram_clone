from rest_framework import serializers

from post_app.models import PostLike
from post_app.serializers.post import UserSerializer


class PostLikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = PostLike
        fields = [
            "id",
            "author",
            "post"
        ]
