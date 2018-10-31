from django.shortcuts import redirect, render
from teamproject.models import *
from accounts.models import *
from hackathon.models import *
import subprocess

# Create your views here.
def main(request, teamId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/main.html', {
            'memberId':request.session['memberId'],
            'teamId':teamId,
            'team':Team.objects.get(pk=teamId),
        })

def notice(request, teamId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/notice.html', {
            'memberId':request.session['memberId'],
            'teamId':teamId,
            'team':Team.objects.get(pk=teamId),
        })

def contribution(request, teamId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/contribution.html', {
            'memberId':request.session['memberId'],
            'teamId':teamId,
            'team':Team.objects.get(pk=teamId),
        })

def chat(request, teamId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/chat.html', {
            'memberId':request.session['memberId'],
            'teamId':teamId,
            'team':Team.objects.get(pk=teamId),
        })

def member(request, teamId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/member.html', {
            'memberId':request.session['memberId'],
            'teamId':teamId,
            'team':Team.objects.get(pk=teamId),
        })

# TODO: create view에서 해커톤 아이디랑 이름 받아와서 해커톤 가능하게 할 수 있겠다.
def create(request):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/create.html', {
            'memberId':request.session['memberId'],
        })

def createWithHackId(request, hackId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        hackTitle = HackathonInformation.objects.get(pk=hackId).title
        return render(request, 'teamproject/create.html', {
            'memberId':request.session['memberId'],
            'hackTitle':hackTitle,
            'hackId':hackId
        })
def process_create(request):

    # exception
    if not 'memberId' in request.session:
        return redirect('/lobby')
    if request.method == 'GET':
        return redirect('/lobby')

    leaderId = request.session['memberId']
    teamName = request.POST['teamName']
    hackId = request.POST['hackId']
    leader = Member.objects.filter(memberId=leaderId)[0]

    team = Team.objects.create(teamName=teamName, leaderId=leader)
    team.save()

    teamContribution = TeamContribution.objects.create(teamId=team)
    teamContribution.save()

    if hackId != "":
        hackathon = HackathonInformation.objects.get(id=hackId)
        participate = Participate.objects.create(memberId=leader, teamId=team, hackId=hackathon)
        participate.save()
        subprocess.call ('~/remote/remote.sh ' + hackId + ' ' + teamName, shell=True)
    else:
        participate = Participate.objects.create(memberId=leader, teamId=team)
        participate.save()
        subprocess.call ('~/remote/remote.sh ' + leaderId + ' ' + teamName, shell=True)
    return redirect('/lobby')
