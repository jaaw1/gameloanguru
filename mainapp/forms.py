from django import forms
from .models import Game, Loan

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'summary', 'status']
        labels = {'name': 'Name:', 'summary': 'Summary:', 'status' : 'status'}
