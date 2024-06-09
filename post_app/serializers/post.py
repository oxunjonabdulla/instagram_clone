from rest_framework import serializers

from post_app.models import Post, PostLike
from users_app.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "image"
        ]


class PostModelSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    post_likes_count = serializers.SerializerMethodField("get_post_likes_count")
    post_comments_count = serializers.SerializerMethodField("get_post_comments_count")
    me_liked = serializers.SerializerMethodField("get_me_liked")

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "text",
            "created_at",
            "post_likes_count",
            "post_comments_count",
            "me_liked"
        ]

        extra_kwargs = {
            "image": {"required": False},
            "text": {"required":False}
        }

    @staticmethod
    def get_post_likes_count(obj):
        return obj.likes.count()

    @staticmethod
    def get_post_comments_count(obj):
        return obj.comments.count()

    def get_me_liked(self, obj):
        request = self.context.get("request", None)
        if request and request.user.is_authenticated:
            try:

                PostLike.objects.get(post=obj, author=request.user)
                return True
            except PostLike.DoesNotExist:
                return False

        return False
