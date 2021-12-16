from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from .models import Game, Loan
from .forms import GameForm, LoanForm

def index(request):
    allgames = Game.objects.order_by('date_added')
    context = {'allgames' : allgames}
    return render(request, 'mainapp/index.html', context)
    
def allgames(request):
    """Show all games."""
    games = Game.objects.order_by('date_added')  
    context = {'games': games}
    return render(request, 'mainapp/allgames.html', context)

@login_required
def mygames(request):
    mygames = Game.objects.filter(owner=request.user).order_by('date_added')
    context = {'mygames' : mygames}
    return render(request, 'mainapp/mygames.html', context)

@login_required
def game(request, game_id):
    """Show a single book and all it's reviews."""
    game = Game.objects.get(id=game_id)
    owner = game.owner
    summary = game.summary
    status = game.status
    #loans = Game.loan_set.order_by('-date_added')
    context = {'game': game, 'summary': summary, 'status': status} #'loans': loans}
    return render(request, 'mainapp/game.html', context)

@login_required
def addgame(request):


    """Add a new game."""
    if request.method != 'POST':
        #No data submitted; create a blank form
        form = GameForm()
    else:
        # POST data submitted; process data.
        form = GameForm(data=request.POST)
        if form.is_valid():
            newgame = form.save(commit=False)
            newgame.owner = request.user
            newgame.save()
            return redirect('mainapp:allgames')
    
    #Display a blank or invalid form.
    context = {'form':form}
    return render(request, 'mainapp/addgame.html', context)

login_required
def editgame(request, game_id):
    """Edit an existing game."""
    
    game = Game.objects.get(id=game_id)
    
    # Make sure the game belongs to the current user.
    if game.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current review.
        form = GameForm(instance=game)
    else:
        # POST data submitted; process data.
        form = GameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:game', game_id=game.id)

    context = {'game' : game, 'form': form}
    return render(request, 'mainapp/editgame.html', context)

def new_loan(request, game_id):
    """Show a loan for a certain game."""
    game = Game.objects.get(id=game_id)
    #loan = Loan.objects.order_by('date_added') 

    if request.method != 'POST':
        #No data submitted; process data.
        form = LoanForm(instance=game)
    else:
        # POST data submitted; process data.
        form = LoanForm(data=request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.owner = request.user
            reserve.game = game

            if loan.action == 'r':
                game.status = 'r'
            elif loan.action == 'l':
                game.status = 'o'
            else:
                game.status = 'a'
            reserve.save()
            return redirect('mainapp:game', game_id=game_id)
    
    #Display a blank or invalid form.
    context = {'game': game, 'form': form}
    return render(request, 'mainapp/reserve.html', context)

@login_required 
def reserve(request, game_id):
    """Add a new reservation to loan a particular boardgame."""
    game = Game.objects.get(id=game_id)
    
    if request.method != 'POST':
        #No data submitted; process data.
        form = LoanForm()
    else:
        # POST data submitted; process data.
        form = LoanForm(data=request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.owner = request.user
            reserve.game = game
            game.status = 'r'
            
            reserve.save()
            return redirect('mainapp:game', game_id=game_id)
    
    #Display a blank or invalid form.
    context = {'game': game, 'form': form}
    return render(request, 'mainapp/reserve.html', context)