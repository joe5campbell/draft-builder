from django.db import models
from django.conf import settings  # Import settings to use AUTH_USER_MODEL

class Game(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='created_games'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    players = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='games'
    )

    def __str__(self):
        return self.name
