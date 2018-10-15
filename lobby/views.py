from django.shortcuts import redirect, render

# Create your views here.
def login(request):
    if not 'memberId' in request.session:
        return render(request, 'lobby/login.html', {
            'numTeamproject' : 3000,
            'numHackathon' : 12345
        })
    else:
        return redirect('/lobby/main')

def main(request):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'lobby/main.html', {'memberId':request.session['memberId']})

def signup(request):
    return lobby(request)
