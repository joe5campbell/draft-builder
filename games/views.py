# games/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game, GuestUser
from .forms import GameForm
from django.http import JsonResponse
from utility_functions.utility_functions import generate_game_code

@login_required
def home(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.creator = request.user
            game.save()
            return redirect('game_detail', game_id=game.id)
    else:
        form = GameForm()

    return render(request, 'draft_builder/home.html', {'form': form})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game_detail.html', {'game': game})




@login_required
def create_game(request):
    if request.method == "POST":
        # Get game details from the request
        name = request.POST.get('name')
        max_players = request.POST.get('max_players', 8)
        
        # Create a new game instance
        game = Game.objects.create(name=name, max_players=max_players, creator=request.user)
        game.save()

        return JsonResponse({"game_code": game.game_code})
    return render(request, 'games/create_game.html')

def join_game(request, game_code):
    if request.method == "POST":
        game = get_object_or_404(Game, game_code=game_code)
        guest_name = request.POST.get('guest_name')

        # Create guest user entry
        guest_user = GuestUser.objects.create(
            game=game,
            guest_id=request.session.session_key,
            guest_name=guest_name
        )
        guest_user.save()

        return redirect('game_detail', game_id=game.id)
    return render(request, 'games/join_game.html')