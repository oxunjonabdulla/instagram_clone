from django.core.validators import FileExtensionValidator, MaxLengthValidator
from django.db import models
from django.db.models import UniqueConstraint

from shared_app.models import BaseModel
from users_app.models import User


# Create your models here.


# User = get_user_model(BaseModel)
class Post(BaseModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to="post_images",
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    text = models.TextField(validators=[MaxLengthValidator(2000)])

    class Meta:
        db_table = "posts"
        verbose_name = "Posts"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"By {self.author.username} :  {self.text[:30] if len(self.text) > 20 else self.text}"


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
        db_table = "post_comment"
        verbose_name = "PostComment"
        verbose_name_plural = "PostComments"

    def __str__(self):
        return f"By {self.author.username} :  {self.text[:30] if len(self.text) > 20 else self.text}"


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
                name="unique_author_post")]
        db_table = "post_like"
        verbose_name = "PostLike"
        verbose_name_plural = "PostLikes"

    def __str__(self):
        return f"By  :  {self.author.username} liked {self.post.text[:30] if len(self.post.text) > 20 else self.post.text}"


class CommentLike(BaseModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment,
                                on_delete=models.CASCADE,
                                related_name="likes")

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["author", "comment"],
                name="unique_author_comment")]
        db_table = "comment_like"
        verbose_name = "CommentLike"
        verbose_name_plural = "CommentLikes"

    def __str__(self):
        return f"By :  {self.author.username} liked {self.comment.text[:30] if len(self.comment.text) > 20 else self.comment.text}"
