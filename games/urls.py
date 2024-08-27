# games/urls.py
from django.urls import path
from .views import home, game_detail

urlpatterns = [
    path('', home, name='home'),  # For showing the game creation form
    path('game/<int:game_id>/', game_detail, name='game_detail'),  # For showing game details
]