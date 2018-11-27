from django.shortcuts import redirect, render
from teamproject.models import Team
from accounts.models import Member, Participate
from hackathon.models import *

# Create your views here.
def login(request):
    if not 'memberId' in request.session:
        result ={'numHackathon': 1234, 'numTeamproject': 30000}
        return render(request, 'lobby/login.html', result)
    else:
        return redirect('/lobby/main')

def main(request):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        member = Member.objects.filter(memberId=request.session['memberId'])
        joinIds = []
        for id in Participate.objects.filter(memberId=member[0]).values('teamId'):
            joinIds.append(id['teamId'])
        joinTeams = Team.objects.filter(id__in=joinIds)
        # 내 해커톤
        hackList = HackathonInformation.objects.filter(participate__memberId=request.session['memberId'])
        return render(request, 'lobby/main.html', {
            'memberId':request.session['memberId'],
            'teams':joinTeams,
            'hackList':hackList
        })

def signup(request):
    return lobby(request)
