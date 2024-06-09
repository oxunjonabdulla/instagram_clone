from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from post_app.models import Post
from post_app.serializers.post import PostModelSerializer


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def put(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.serializer_class(instance=post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "Post successfully updated",
                "status_code": status.HTTP_200_OK,
                "data": serializer.data
            }
        )

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if post:
            post.delete()
            return Response({
                "success": True,
                "message": "Post successfully deleted",
                "status_code": status.HTTP_204_NO_CONTENT
            })
        return Response({
            "success": False,
            "message": "Post not found",
            "status_code": status.HTTP_404_NOT_FOUND
        })
