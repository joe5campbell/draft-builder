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
        name = request.POST.get('name')
        max_players = request.POST.get('max_players')
        draft_settings = request.POST.get('draft_settings')

        game = Game.objects.create(
            name=name,
            max_players=max_players,
            draft_settings=draft_settings,
            creator=request.user
        )
        game.game_code = generate_game_code()  # Implement this function
        game.save()

        return JsonResponse({"game_code": game.game_code})

def join_game(request, game_code):
    if request.method == "POST":
        game = get_object_or_404(Game, game_code=game_code)
        guest_name = request.POST.get('guest_name')

        guest_user = GuestUser.objects.create(
            game=game,
            guest_id=request.session.session_key,
            guest_name=guest_name
        )
        
        return JsonResponse({"message": "Successfully joined the game."})