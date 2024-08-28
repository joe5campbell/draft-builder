# games/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game, GuestUser
from .forms import GameForm
from django.http import JsonResponse
from utility_functions.utility_functions import generate_game_code

@login_required(login_url='login')
def create_game(request):
    if request.method == "POST":
        # Get game details from the request
        name = request.POST.get('name')
        max_players = request.POST.get('max_players', 8)
        player_name = request.POST.get('player_name')
        
        # Create a new game instance
        game = Game.objects.create(name=name, max_players=max_players, creator=request.user)
        
        # Add the game creator as a player
        guest_user = GuestUser.objects.create(
            game=game,
            guest_id=request.session.session_key,
            guest_name=player_name
        )

        # Correct the missing return statement
        return redirect('game_detail', game_id=game.id)
    
    return render(request, 'create_game.html')

def join_game(request, game_code = ""):
    if request.method == "POST":
        game_code = request.POST.get('game_code')
        game = get_object_or_404(Game, game_code=game_code)
        guest_name = request.POST.get('guest_name')

        # Ensure the session key exists
        if not request.session.session_key:
            request.session.create()

        # Create guest user entry
        guest_user = GuestUser.objects.create(
            game=game,
            guest_id=request.session.session_key,
            guest_name=guest_name
        )
        guest_user.save()

        return redirect('game_detail', game_id=game.id)
    
    return render(request, 'join_game.html', {'game_code': game_code})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game_detail.html', {'game': game})

def game_players(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    players = list(game.guestuser_set.values('guest_name'))
    return JsonResponse({'players': players})

