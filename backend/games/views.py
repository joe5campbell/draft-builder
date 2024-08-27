from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Game
from .serializers import GameSerializer

class GameCreateView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user, players=[self.request.user])