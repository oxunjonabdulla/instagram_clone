from rest_framework import serializers

from post_app.models import PostComment
from post_app.serializers.post import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField("get_replies")
    me_liked = serializers.SerializerMethodField("get_me_liked")
    likes_count = serializers.SerializerMethodField("get_likes_count")

    class Meta:
        model = PostComment
        fields = [
            "id",
            "author",
            "text",
            "post",
            "parent",
            "created_at",
            "replies",
            "me_liked",
            "likes_count"
        ]

    def get_replies(self, obj):
        if obj.child.exists():
            serializer = self.__class__(obj.child.all(), many=True,
                                        context=self.context)
            return serializer.data
        else:
            return None

    def get_me_liked(self, obj):
        user = self.context.get("request").user
        if user.is_authenticated:
            return obj.likes.filter(author=user).exists()
        else:
            return False

    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()
