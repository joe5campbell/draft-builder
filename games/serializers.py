from rest_framework import serializers
from .models import Game

from rest_framework import serializers
from .models import Game, GuestUser

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'max_players', 'draft_settings', 'creator', 'game_code']

class GuestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestUser
        fields = ['id', 'game', 'guest_id', 'guest_name', 'is_active']