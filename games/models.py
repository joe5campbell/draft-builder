from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Game(models.Model):
    name = models.CharField(max_length=100)
    max_players = models.IntegerField(default=8)
    draft_settings = models.JSONField(default=dict)  # Default value for draft_settings
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game_code = models.CharField(max_length=10, unique=True, default='TEMP')  # Temporary default to pass migrations

class GuestUser(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    guest_id = models.CharField(max_length=100)
    guest_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)