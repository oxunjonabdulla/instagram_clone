from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from post_app.models import PostLike, CommentLike
from post_app.serializers.comment_like import CommentLikeModelSerializer
from post_app.serializers.post_like import PostLikeSerializer


class PostLikeAPIView(APIView):

    def post(self, request, pk):
        try:
            post_like = PostLike.objects.get(author=self.request.user,
                                             post_id=pk)
            post_like.delete()
            data = {
                "success": True,
                "message": "Successfully post_like deleted"
            }
            return Response(
                data=data,
                status=status.HTTP_204_NO_CONTENT
            )
        except PostLike.DoesNotExist:
            post_like = PostLike.objects.create(
                author=self.request.user,
                post_id=pk
            )
            serializer = PostLikeSerializer(post_like)
            data = {
                "success": False,
                "message": "post like successfully created",
                "data": serializer.data
            }
            return Response(
                data=data,
                status=status.HTTP_201_CREATED,

            )


class CommentLikeApiView(APIView):

    def post(self, request, pk):
        try:
            comment_like = CommentLike.objects.get(
                author=self.request.user,
                comment_id=pk
            )
            comment_like.delete()
            data = {
                "success": True,
                "message": "Successfully comment_like deleted"
            }
            return Response(
                data=data,
                status=status.HTTP_204_NO_CONTENT
            )
        except CommentLike.DoesNotExist:
            comment_like = CommentLike.objects.create(
                author=self.request.user,
                comment_id=pk
            )
            serializer = CommentLikeModelSerializer(comment_like)
            data = {
                "success": False,
                "message": "comment like successfully created",
                "data": serializer.data
            }
            return Response(
                data=data,
                status=status.HTTP_201_CREATED,
            )
