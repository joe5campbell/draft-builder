from django.contrib.auth.models import AbstractUser
from django.db import models

class DraftBuilderUser(AbstractUser):
    # Additional fields
    display_name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    # Other fields can be added as needed based on future requirements

    def __str__(self):
        return self.username