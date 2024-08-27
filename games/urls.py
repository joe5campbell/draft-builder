# games/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_game/', views.create_game, name='create_game'),
    path('join_game/<str:game_code>/', views.join_game, name='join_game'),
]