from django.shortcuts import redirect, render
from teamproject.models import Team
from accounts.models import Member, Participate

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
        member = Member.objects.filter(memberId=request.session['memberId'])
        print(member)
        joinIds = []
        for id in Participate.objects.filter(memberId=member[0]).values('teamId'):
            joinIds.append(id['teamId'])
        print(joinIds)
        joinTeams = Team.objects.filter(id__in=joinIds)
        print(joinTeams)
        return render(request, 'lobby/main.html', {
            'memberId':request.session['memberId'],
            'teams':joinTeams,
        })

def signup(request):
    return lobby(request)
