from django.shortcuts import render, redirect
from games.forms import GameForm

def home(request):
    return render(request, 'draft_builder/home.html')
