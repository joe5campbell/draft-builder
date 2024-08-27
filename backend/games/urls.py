from django.urls import path
from .views import GameCreateView

urlpatterns = [
    path('create/', GameCreateView.as_view(), name='create-game'),
]