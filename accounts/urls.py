# accounts/urls.py
from django.urls import path, include
from .views import register #, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    # path('profile/', profile, name='profile'),  # Add this line 
]