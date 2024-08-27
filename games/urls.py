# games/urls.py
from django.urls import path
from .views import home, game_detail

urlpatterns = [
    path('start/', home, name='game_start'),  # This should point to the home view for starting a game
    path('detail/<int:game_id>/', game_detail, name='game_detail'),
]