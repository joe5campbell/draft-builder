from django.urls import path
from . import views

urlpatterns = [
    path('create_game/', views.create_game, name='create_game'),
    path('join_game/<str:game_code>/', views.join_game, name='join_game'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('create_game/', views.create_game, name='create_game'),
    path('join_game/<str:game_code>/', views.join_game, name='join_game'),
    path('game/<int:game_id>/players/', views.game_players, name='game_players'), 
]