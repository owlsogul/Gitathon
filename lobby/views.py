from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'lobby/login.html', {
        'numTeamproject' : 3000,
        'numHackathon' : 12345
    })

def main(request):
    return render(request, 'lobby/main.html', {})

def signup(request):
    return lobby(request)
