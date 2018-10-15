from django.shortcuts import redirect, render
from teamproject.models import *
from accounts.models import *

# Create your views here.
def main(request, teamId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/main.html', {
            'memberId':request.session['memberId'],
            'teamId':teamId,
        })

# TODO: create view에서 해커톤 아이디랑 이름 받아와서 해커톤 가능하게 할 수 있겠다.
def create(request):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/create.html', {
            'memberId':request.session['memberId'],
        })

def process_create(request):

    # exception
    if not 'memberId' in request.session:
        return redirect('/lobby')
    if request.method == 'GET':
        return redirect('/lobby')

    leaderId = request.session['memberId']
    teamName = request.POST['teamName']
    leader = Member.objects.filter(memberId=leaderId)[0]

    team = Team.objects.create(teamName=teamName, leaderId=leader)
    team.save()

    teamContribution = TeamContribution.objects.create(teamId=team)
    teamContribution.save()

    if 'hackId' in request.POST:
        participate = Participate.objects.create(memberId=leader, teamId=team, hackId=request.POST['hackId'])
        participate.save()
    else:
        participate = Participate.objects.create(memberId=leader, teamId=team)
        participate.save()
    return redirect('/lobby')
