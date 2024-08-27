# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DraftBuilderUser  # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = DraftBuilderUser  # Use your custom user model here
        fields = ('username', 'email', 'password1', 'password2')  # Include other fields as needed

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user