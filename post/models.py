from django.core.validators import FileExtensionValidator, MaxLengthValidator
from django.db import models
from django.db.models import UniqueConstraint

from shared.models import BaseModel
from users.models import User


# Create your models here.


# User = get_user_model(BaseModel)
class Post(BaseModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images",
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    text = models.TextField(validators=[MaxLengthValidator(2000)])

    class Meta:
        db_table = "posts"
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.text


class PostComment(BaseModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    text = models.TextField(validators=[MaxLengthValidator(1000)])
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="child",
        null=True, blank=True
    )

    class Meta:
        db_table = "postComment"
        verbose_name = "postComment"
        verbose_name_plural = "postComments"

    def __str__(self):
        return self.text


class PostLike(BaseModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="likes")

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["author", "post"],
                name="unique_author_post"
            )
        ]
        db_table = "postLike"
        verbose_name = "postLike"
        verbose_name_plural = "postLikes"

    def __str__(self):
        return self.post.text


class CommentLike(BaseModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment,
                                on_delete=models.CASCADE,
                                related_name="likes")

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=[
                    "author", "comment"
                ],
                name="unique_author_comment"
            )
        ]
        db_table = "CommentLike"
        verbose_name = "CommentLike"
        verbose_name_plural = "CommentLikes"

    def __str__(self):
        return self.comment.text
