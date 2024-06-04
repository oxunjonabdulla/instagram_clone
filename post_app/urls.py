from django.urls import path

from post_app.views.post import PostListAPIView

urlpatterns = [
    path("post_list/", PostListAPIView.as_view(), name='post')
]
