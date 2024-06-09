from django.urls import path

from post_app.views.comment.create import PostCommentCreateAPIView
from post_app.views.comment.list import PostCommentListAPIView, CommentListCreateAPIView
from post_app.views.comment.retrieve import PostCommentRetrieveAPIView
from post_app.views.like.create import PostLikeCreateAPIView, CommentLikeCreateApiView
from post_app.views.like.create_delete_like_with_api_view import PostLikeAPIView, CommentLikeApiView
from post_app.views.like.delete import PostLikeDestroyAPIView, CommentLikeDestroyAPIView
from post_app.views.like.list import PostLikeListAPIView, CommentLikeListAPIView
from post_app.views.post.create import PostCreateAPIView
from post_app.views.post.get_update_delete import PostRetrieveUpdateDestroyAPIView
from post_app.views.post.list import PostListAPIView

urlpatterns = [
    path("list/", PostListAPIView.as_view()),
    path("create/", PostCreateAPIView.as_view()),

    path("<uuid:pk>/", PostRetrieveUpdateDestroyAPIView.as_view()),
    path("<uuid:pk>/create-delete-like/", PostLikeAPIView.as_view()),
    path("<uuid:pk>/comments/", PostCommentListAPIView.as_view()),

    path("<uuid:pk>/comments/create/", PostCommentCreateAPIView.as_view()),
    path("comments/", CommentListCreateAPIView.as_view()),

    path("comments/<uuid:pk>/", PostCommentRetrieveAPIView.as_view()),
    path("comments/<uuid:pk>/create-delete-like/", CommentLikeApiView.as_view()),

    path("<uuid:pk>/likes/", PostLikeListAPIView.as_view()),
    path('<uuid:pk>/likes/create/', PostLikeCreateAPIView.as_view()),

    path('<uuid:pk>/likes/<uuid:post_like_pk>/', PostLikeDestroyAPIView.as_view()),


    path("comments/<uuid:pk>/likes/", CommentLikeListAPIView.as_view()),
    path("comments/<uuid:pk>/likes/delete/<uuid:comment_like_pk>/", CommentLikeDestroyAPIView.as_view()),
    path("comments/<uuid:pk>/likes/create/", CommentLikeCreateApiView.as_view()),


]
