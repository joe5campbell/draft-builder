from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import random
import string

class Game(models.Model):
    name = models.CharField(max_length=100)
    max_players = models.IntegerField(default=8)
    draft_settings = models.JSONField(default=dict)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game_code = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.game_code:
            self.game_code = self.generate_unique_game_code()
        super(Game, self).save(*args, **kwargs)

    def generate_unique_game_code(self):
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if not Game.objects.filter(game_code=code).exists():
                break
        return code

class GuestUser(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    guest_id = models.CharField(max_length=100)
    guest_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)