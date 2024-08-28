"""draft_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from games import views as games_views  # Correct imports from games/views
from django.contrib.auth import views as auth_views
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Home page for starting a game
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),  # Include games' URL configuration
    path('accounts/', include('accounts.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_game/', games_views.create_game, name='create_game'),
    path('join_game/', games_views.join_game, name='join_game'),
]