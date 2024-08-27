# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    # Make sure this path matches your actual template directory
    return render(request, 'registration/register.html', {'form': form})

# @login_required
# def profile(request):
#     return render(request, 'registration/profile.html')  # Create this template file
