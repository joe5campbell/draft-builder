from django.shortcuts import render, redirect
from games.forms import GameForm

def home(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.creator = request.user
            game.save()
            return redirect('game_start', game_id=game.id)
    else:
        form = GameForm()
    
    return render(request, 'draft_builder/home.html', {'form': form}) 
