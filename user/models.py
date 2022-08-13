import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class SocialUser(AbstractUser):
    id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email             = models.EmailField(unique=True)
    first_name        = models.CharField(max_length=64)
    last_name         = models.CharField(max_length=64, blank=True)
    password          = models.CharField(max_length=256)
    username          = models.CharField(unique=True, max_length=64)
    profile_image     = models.URLField(null=True, blank=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    is_email_verified = models.BooleanField(default=False)
    is_staff          = models.BooleanField(default=False)
    is_superuser      = models.BooleanField(default=False)
    is_superuser      = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def json(self):
        return {
            "id": str(self.id),
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "profile_image": self.profile_image,
            "username": self.username
        }
