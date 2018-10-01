from django.shortcuts import render

# Create your views here.
def lobby(request):
    return render(request, 'lobby/lobby.html', {
        'numTeamproject' : 3000,
        'numHackathon' : 12345
    })
