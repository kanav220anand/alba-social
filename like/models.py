import uuid

from django.db import models
from post.models import Post
# from user.models import SocialUser
from django.contrib.auth import get_user_model
User= get_user_model()


class Like(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "like"
