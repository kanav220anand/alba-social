import uuid

from django.db import models
# from user.models import SocialUser
from django.contrib.auth import get_user_model
User= get_user_model()


class Post(models.Model):
	id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	content       = models.TextField(blank=True)
	created_at    = models.DateTimeField(auto_now_add=True)
	author        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	numberOfLikes = models.IntegerField(default=0, null=True, blank=True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
