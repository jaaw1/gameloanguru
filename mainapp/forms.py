from django import forms
from .models import Game, Loan

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name']
        labels = {'name': 'Name:'}
