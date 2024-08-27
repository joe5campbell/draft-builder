from django.contrib.auth.models import AbstractUser
from django.db import models

class draft_builder_user(AbstractUser):
    # Additional fields
    display_name = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    # Other fields can be added as needed based on future requirements

    def __str__(self):
        return self.username