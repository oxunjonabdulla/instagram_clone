from django.contrib import admin

from post_app.models import Post, PostComment, PostLike, CommentLike


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "text", "image"]
    list_filter = ["author"]
    search_fields = ["id", 'text', 'author__username']


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "post", "text", "parent"]
    list_filter = ["author"]
    search_fields = ['text', 'author__username']


class PostLikeAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "post"]
    list_filter = ["author"]
    search_fields = ['post', 'author__username']


class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "comment"]
    list_filter = ["author"]
    search_fields = ['comment', 'author__username']


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)
