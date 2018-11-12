from django.shortcuts import redirect, render
from teamproject.models import *
from accounts.models import *
from hackathon.models import *

from teamproject import parseGit
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
        memberId = request.session['memberId']
        member = Member.objects.get(pk=memberId)
        team = Team.objects.get(pk=teamId)
        teamContribution = TeamContribution.objects.get(teamId = team)

        participate = Participate.objects.get(memberId=member, teamId=team)
        hackName = memberId
        if participate.hackId is not None:
            hackName = participate.hackId.pk

        resourceList = ["jpg", "png"]
        parsingData = parseGit.parseGit(hackName, team.teamName, "", resourceList)
        print(parsingData)

        class ContributionData:
            memberId = ""
            code = 0
            comment = 0
            resource = 0
            total = 0

        contributions = []
        participate = Participate.objects.filter(teamId=team)
        for p in participate:
            contributionData = ContributionData()
            contributionData.memberId = p.memberId.memberId
            contributions.append(contributionData)

        return render(request, 'teamproject/contribution.html', {
            'memberId':memberId,
            'teamId':teamId,
            'team':team,
            'comment':teamContribution.comment,
            'code':teamContribution.code,
            'resource':teamContribution.resource,
<<<<<<< HEAD
            'contributions':contributions,
=======
            'test': parsingData,
>>>>>>> bd1c16b580b27311494b5ea16a65f187c0bbdd37
        })

def chat(request, teamId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        team = Team.objects.get(pk=teamId)
        chatMsgs = TeamChat.objects.filter(teamId = team)
        return render(request, 'teamproject/chat.html', {
            'memberId':request.session['memberId'],
            'teamId':teamId,
            'team':team,
            'chatMsgs':chatMsgs,
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
        # 삭제하고 다시 생성하는 과정!
        Participate.objects.get(memberId = leader, hackId = hackathon).delete()
        participate = Participate.objects.create(memberId=leader, teamId=team, hackId=hackathon)
        participate.save()
        subprocess.call ('/home/pi/remote/remote.sh ' + hackId + ' ' + teamName, shell=True)
    else:
        participate = Participate.objects.create(memberId=leader, teamId=team)
        participate.save()
        subprocess.call ('/home/pi/remote/remote.sh ' + leaderId + ' ' + teamName, shell=True)
    return redirect('/lobby')
